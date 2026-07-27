from database import engine,SessionLocal
from databasemodel import Base
from fastapi import FastAPI, Depends

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
