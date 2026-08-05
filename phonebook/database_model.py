from phonebook.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from pydantic import BaseModel


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    hashed_password = Column(String)
    
class UserRequest(BaseModel):
    username:str
    password:str
    
class UserResponse(BaseModel):
    id:int
    username:str

class PhoneBook(Base):
    __tablename__ = "phonebook"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id"))
    
class PhoneRequest(BaseModel):
    name: str
    number: str
    