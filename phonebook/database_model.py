from phonebook.database import Base
from sqlalchemy import Column,String,Integer
from pydantic import BaseModel

class PhoneBook(Base):
    __tablename__ = "phonebook"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)
    
class PhoneRequest(BaseModel):
    name: str
    number: int
    