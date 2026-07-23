from fastapi import FastAPI
from contact_api.contactroutes import router

app = FastAPI()

app.include_router(router)