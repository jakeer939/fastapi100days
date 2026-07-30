from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from phonebook.database import engine,sessionLocal
from phonebook.database_model import Base,PhoneBook,PhoneRequest

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"homepage"}