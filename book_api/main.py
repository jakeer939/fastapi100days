from fastapi import FastAPI
from books import router

app = FastAPI()
app.include_router(router)