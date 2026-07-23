from pydantic import BaseModel,EmailStr

class Contacts(BaseModel):
    name: str
    phone: str
    email: EmailStr
    city: str
    favorite: bool