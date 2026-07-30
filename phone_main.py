from fastapi import FastAPI,Depends
from sqlalchemy.orm import sessionmaker,Session
from phonebook.database import engine,sessionLocal
from phonebook.database_model import Base,PhoneBook,PhoneRequest

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"homepage"}

@app.post("/phonebook")
def create_contact(contact:PhoneRequest,db:Session = Depends(get_db)):
    new_contact = PhoneBook(**contact.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"new contact":new_contact}

@app.get("/phonebook")
def get_all_contacts(db:Session = Depends(get_db)):
    data = db.query(PhoneBook).all()
    return data