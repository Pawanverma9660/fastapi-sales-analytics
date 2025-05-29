from fastapi import FastAPI
from app import auth, sales
from app.database import init_db

app = FastAPI()

init_db()

app.include_router(auth.router)
app.include_router(sales.router)
