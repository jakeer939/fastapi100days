from typing import List

from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from phonebook.database import sessionLocal
from phonebook.database_model import Base,PhoneBook,PhoneRequest
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/phonebook",
    tags=["Phonebook api"]
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[PhoneRequest])
async def get_all_contacts(db:Session=Depends(get_db)):
    contacts = db.scalars(select(PhoneBook)).all()
    if contacts is None:
        raise HTTPException(status_code=404, detail="data not found")
    return contacts

@router.post("/",response_model=PhoneRequest)
async def create_contact(contact:PhoneRequest, db:Session=Depends(get_db)):
    c = PhoneBook(**contact.model_dump())
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@router.put("/{contact_id}",response_model = PhoneRequest)
async def updatecontact(contact_id:int, contact:PhoneRequest, db:Session = Depends(get_db)):
    c = db.scalar(select(PhoneBook).where(PhoneBook.id == contact_id))
    if c is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    c.name = contact.name
    c.number = contact.number    
    db.commit()
    db.refresh(c)
    return c

@router.delete("/{contact_id}",response_model=PhoneRequest)
async def deletecontact(contact_id:int,db:Session=Depends(get_db)):
    contact = db.scalar(select(PhoneBook).where(PhoneBook.id == contact_id))
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return contact