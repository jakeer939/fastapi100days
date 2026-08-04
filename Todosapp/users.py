from Todosapp.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Todosapp.databasemodel import Users
from sqlalchemy import select
from .auth import get_current_user
from passlib.context import CryptContext
from pydantic import BaseModel


bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated="auto")
router = APIRouter(
    prefix="/user",
    tags=["User"]
)

class UserVerification(BaseModel):
    password:str
    new_password:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def get_user(user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    return db.scalar(select(Users).where(user["id"]==Users.id))

@router.put("/")
def update_pass(us:UserVerification,user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_model = db.scalar(select(Users).where(user["id"]==Users.id))
    if not bcrypt_context.verify(us.password,user_model.hashed_password):
        raise HTTPException(status_code=401, detail="error on password change")
    user_model.hashed_password = bcrypt_context.hash(us.new_password)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    raise HTTPException(status_code=203,detail="updated successfully")
    
    

        
        