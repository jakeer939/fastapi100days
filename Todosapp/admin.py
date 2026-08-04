
from sqlalchemy import select
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Todosapp import databasemodel
from Todosapp.database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix="/admin/todo",
    tags=["admin"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def get_all_todos(user:dict=Depends(get_current_user), db:Session=Depends(get_db)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="admin previlages required")
    return db.scalars(select(databasemodel.Todos)).all()

@router.delete("/{todo_id}")
def delete_todo(todo_id:int, user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    if user["role"]!= "admin":
        raise HTTPException(status_code=403,detail="admin previlages required")
    todo = db.scalar(select(databasemodel.Todos).where(todo_id==databasemodel.Todos.id))
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    db.delete(todo)
    db.commit()
    return todo