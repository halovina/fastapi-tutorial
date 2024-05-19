from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Users
from db_config import get_db


router = APIRouter(
    prefix='/users',
    tags=['users'], #tags url
    responses= {404: {'message': 'Not found'}},
)

@router.get("/")
def get_all_users(db: Session=Depends(get_db)):
    users = db.query(Users).all()
    return users