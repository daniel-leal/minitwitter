import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from routers import users

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(
    DBSessionMiddleware, db_url=os.environ["SQLALCHEMY_DATABASE_URI"]
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(users.router)
