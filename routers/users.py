from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import models, crud
from db_config import get_db
from schema import users as schemas


router = APIRouter(
    prefix='/users',
    tags=['users'], #tags url
    responses= {404: {'message': 'Not found'}},
)

@router.get("/")
def get_all_users(page: int=0, limit: int=10, db: Session=Depends(get_db)):
    return crud.get_user_by_limit_offset(db, page=page, page_limit=limit)


@router.get("/{user_id}")
def get_all_users(user_id: int, db: Session=Depends(get_db)):
    return crud.get_user_byid(db, user_id)


@router.post("/create-user")
def create_new_user(user: schemas.CreateUser, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email_username(db, email=user.email, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email and username already registered")
    return crud.create_new_user(db, user=user)