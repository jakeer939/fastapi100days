from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Contacts(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    city = Column(String)
    favorite = Column(Boolean)