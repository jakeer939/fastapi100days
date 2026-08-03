from sqlalchemy import select
from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from Todosapp import databasemodel
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from Todosapp.database import SessionLocal

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated="auto")


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    role: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

        
@router.get("/auth",response_model=List[UserResponse])
async def get_all_users(db:Session = Depends(get_db)):
    users = db.scalars(select(databasemodel.Users)).all()
    return users

@router.post("/auth/",response_model=UserResponse)
async def createuser(user_req : databasemodel.UserRequest, db:Session = Depends(get_db)):
    user = databasemodel.Users(
        email = user_req.email,
        first_name = user_req.first_name,
        last_name = user_req.last_name,
        username = user_req.username,
        role = user_req.role,
        hashed_password = bcrypt_context.hash(user_req.password),
        is_active = True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate (username:str, password:str, db):
    user = db.query(databasemodel.Users).filter(databasemodel.Users.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return True
        
@router.post("/token")
async def login_token(form_data:OAuth2PasswordRequestForm = Depends( ), db:Session = Depends(get_db)):
    data = authenticate(form_data.username, form_data.password, db)
    if not data:
        return "authentication failed"
    return "authentication successful"

        