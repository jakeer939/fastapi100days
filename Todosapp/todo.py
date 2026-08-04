from Todosapp.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Todosapp.databasemodel import Todos,TodoRequest
from sqlalchemy import select
from .auth import get_current_user
router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.get("/",response_model=TodoRequest)
def get_all_todos(db:Session=Depends(get_db),user:dict = Depends(get_current_user)):
    todo = db.scalars(select(Todos).where(Todos.owner_id==user["id"])).all()
    return todo

@router.get("/{todo_id}",response_model=TodoRequest)
def get_todo(todo_id:int, db:Session=Depends(get_db),user:dict=Depends(get_current_user)):
    todo = db.scalars(select(Todos).where(todo_id==Todos.id,user["id"] == Todos.owner_id)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="data not found")
    return todo

@router.post("/",response_model=TodoRequest)
def add_todo(todo:TodoRequest,user:dict = Depends(get_current_user), db:Session=Depends(get_db)):
    
    new_todo = Todos(**todo.model_dump(),owner_id = user["id"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/{todo_id}",response_model=TodoRequest)
def update_todo(todo_id:int,new_todo:TodoRequest,db:Session = Depends(get_db),user:dict = Depends(get_current_user)):
    todo = db.scalars(select(Todos).where(todo_id==Todos.id,user["id"] == Todos.owner_id)).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    todo.title = new_todo.title
    todo.priority = new_todo.priority
    todo.complete = new_todo.complete
    todo.description = new_todo.description
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}",response_model=TodoRequest)
def delete_todo(todo_id:int, db:Session=Depends(get_db),user:dict = Depends(get_current_user)):
    todo = db.scalar(select(Todos).where(todo_id==Todos.id,user["id"] == Todos.owner_id))
    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo