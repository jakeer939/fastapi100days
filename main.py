from Todosapp.database import engine
from Todosapp.databasemodel import Base
from fastapi import FastAPI
from Todosapp import auth
from Todosapp import todo
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todo.router)
