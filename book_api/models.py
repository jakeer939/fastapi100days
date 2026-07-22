from pydantic import BaseModel
class Book(BaseModel):
    name:str
    author:str
    published_year:int
    country:str
    language:str
    price:int