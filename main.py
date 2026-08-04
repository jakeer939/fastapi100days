from Todosapp.database import engine
from Todosapp.databasemodel import Base
from fastapi import FastAPI
from Todosapp import auth
from Todosapp import todo
from Todosapp import admin
from Todosapp import users
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(admin.router)
app.include_router(users.router)
