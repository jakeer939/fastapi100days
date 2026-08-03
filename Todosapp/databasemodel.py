from Todosapp.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from pydantic import BaseModel


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String, unique=True)
    username = Column(String,unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    
class UserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey("users.id") )
    
class TodoRequest(BaseModel):
    title :str
    description : str
    priority : int 
    complete : bool
    