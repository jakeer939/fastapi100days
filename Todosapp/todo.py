from Todosapp.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Todosapp.databasemodel import Todos,TodoRequest
from sqlalchemy import select
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.get("/todos")
def get_all_todos(db:Session=Depends(get_db)):
    todo = db.scalars(select(Todos)).all()
    return todo

@router.get("/todos/{todo_id}")
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.get(Todos,todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="data not found")
    return todo

@router.post("/todos",response_model=TodoRequest)
def add_todo(todo:TodoRequest, db:Session=Depends(get_db)):
    new_todo = Todos(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/todos/{todo_id}")
def update_todo(todo_id:int,new_todo:TodoRequest,db:Session = Depends(get_db)):
    todo = db.get(Todos,todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="id not found")
    todo.title = new_todo.title
    todo.priority = new_todo.priority
    todo.complete = new_todo.complete
    todo.description = new_todo.description
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.get(Todos, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="id not found")
    db.delete(todo)
    db.commit()
    return todo