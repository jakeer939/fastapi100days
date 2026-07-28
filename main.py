from database import engine,SessionLocal
from databasemodel import Base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from databasemodel import Todos,TodoRequest
from sqlalchemy import select
app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.get("/todos")
def get_all_todos(db:Session=Depends(get_db)):
    todo = db.scalars(select(Todos)).all()
    return todo

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.get(Todos,todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="data not found")
    return todo

@app.post("/todos",response_model=TodoRequest)
def add_todo(todo:TodoRequest, db:Session=Depends(get_db)):
    new_todo = Todos(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put("/todos/{todo_id}")
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

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.get(Todos, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="id not found")
    db.delete(todo)
    db.commit()
    return todo
    
