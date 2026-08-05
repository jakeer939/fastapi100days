
from fastapi import FastAPI
from phonebook.database_model import Base
from phonebook.database import engine
from phonebook import endpoints
from phonebook import authendpoints

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(endpoints.router)
app.include_router(authendpoints.router)
