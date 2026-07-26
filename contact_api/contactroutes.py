from fastapi import APIRouter,HTTPException,status,Depends
from contact_api.database import contacts
from contact_api.models import Contacts

router = APIRouter()

def id_val():
    mx_id = 0
    for contact in contacts:
        if contact["id"]>mx_id:
            mx_id = contact["id"]
    return mx_id+1

@router.get("/")
def home():
    return {"message":"this is fastapi's contact api"}

@router.get("/contacts")
def get_all_contacts():
    return contacts

@router.get("/contacts/{user_id}")
def get_user(user_id:int):
    for contact in contacts:
        if contact["id"] == user_id:
            return contact
    raise HTTPException(status_code=404,detail="not found")

@router.post("/contacts",status_code=status.HTTP_201_CREATED)
def add_user(contact:Contacts, id_n:int = Depends(id_val)):
    if(len(contact.phone)==10 and contact.phone.isdigit()):
        new_val = {
            "id":id_n,
            **contact.model_dump()
        }
        contacts.append(new_val)
        return new_val
    raise HTTPException(status_code=400, detail="bad request")

@router.put("/contacts/{user_id}")
def update_user(contact:Contacts,user_id:int):
    if len(contact.phone)!=10 and contact.phone.isdigit():
        raise HTTPException(status_code=400,detail="bad request")
    for c in contacts:
        if c["id"] == user_id:
            c["name"] = contact.name
            c["phone"] = contact.phone
            c["email"] = contact.email
            c["city"] = contact.city
            c["favorite"] = contact.favorite
            return c
    raise HTTPException(status_code=404,detail="id not found")

@router.delete("/contacts/{user_id}")
def delete_user(user_id:int):
    for contact in contacts:
        if contact["id"] == user_id:
            contacts.remove(contact)
            return contact
    raise HTTPException(status_code=404, detail="not found")


        
