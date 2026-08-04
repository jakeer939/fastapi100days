from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from typing import List

from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from Todosapp import databasemodel
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Todosapp.database import SessionLocal
from jose import jwt,JWTError

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)
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
        

SECRET_KEY = "b8d5f0de4409142d48b3258b854d09277e7166b2bb1f7f20d1228a30736891e9"
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/token')

def create_token(username: str, user_id: int, user_role: str, expire_delta: timedelta):
    payload = {"sub": username, "id": user_id, "role": user_role}
    expires = datetime.now(timezone.utc) + expire_delta
    payload.update({"exp": int(expires.timestamp())})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role:str = payload.get("role")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate")
        user = db.get(databasemodel.Users, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate")
        return {"id": user.id, "username": user.username, "email": user.email, "role": user.role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate")
        
        
@router.get("/",response_model=List[UserResponse])
async def get_all_users(db:Session = Depends(get_db)):
    users = db.scalars(select(databasemodel.Users)).all()
    return users

@router.post("/",response_model=UserResponse)
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

def authenticate(username: str, password: str, db):
    user = db.query(databasemodel.Users).filter(databasemodel.Users.username == username).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user
        
@router.post("/token")
async def login_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_token(user.username, user.id,user.role, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}

        