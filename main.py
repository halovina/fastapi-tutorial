from typing import Union

from fastapi import FastAPI, Depends
from db_config import get_db
from models import Users
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_all_users(db: Session=Depends(get_db)):
    users = db.query(Users).all()
    return users