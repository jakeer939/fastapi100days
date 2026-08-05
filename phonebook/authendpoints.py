from typing import List

from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from phonebook.database import sessionLocal
from phonebook.database_model import Users,UserRequest,UserResponse
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix="/users",
    tags=["users api"]
)

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[UserResponse])
async def get_all_users(db:Session=Depends(get_db)):
    users = db.scalars(select(Users)).all()
    if users is None:
        raise HTTPException(status_code=404, detail="data not found")
    return users

@router.post("/",response_model=UserResponse)
async def create_user(user:UserRequest, db:Session=Depends(get_db)):
    us = Users(
        username = user.username,
        hashed_password = bcrypt_context.hash(user.password)
               )
    db.add(us)
    db.commit()
    db.refresh(us)
    return us