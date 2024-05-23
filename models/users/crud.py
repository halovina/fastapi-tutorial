from sqlalchemy.orm import Session
from . import models
from schema import users as schemas

def get_user_by_email_username(db: Session, email: str, username: str):
    return db.query(models.Users).filter(
        models.Users.email == email,
        models.Users.username == username
    ).first()
    
def create_new_user(db: Session, user: schemas.CreateUser):
    db_user = models.Users(
        email= user.email,
        username= user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_user_byid(db:Session, user_id: int):
    return db.query(models.Users).filter(
        models.Users.id == user_id
    ).first()
    
def get_user_by_limit_offset(db: Session, page: int, page_limit: int):
    return db.query(models.Users).limit(page_limit).offset(page*page_limit).all()