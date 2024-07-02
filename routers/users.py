from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, responses
from sqlalchemy.orm import Session
from models.users import models, crud
from db_config import get_db
from schema import users as schemas
from typing import Annotated
import re
from models.users import sqlm_users
from schema import scm_sqlmodel


router = APIRouter(
    prefix='/users',
    tags=['users'], #tags url
    responses= {404: {'message': 'Not found'}},
)

def is_valid_email(email):
    """
    Checks if the given email is valid.

    Args:
        email (str): The email address to check.

    Returns:
        bool: True if the email is valid, False otherwise.
    """

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

@router.get("/")
def get_all_users(page: int=0, limit: int=10, db: Session=Depends(get_db)):
    return crud.get_user_by_limit_offset(db, page=page, page_limit=limit)


@router.get("/{user_id}")
def get_all_users(user_id: int, db: Session=Depends(get_db)):
    return crud.get_user_byid(db, user_id)


@router.post("/create-user")
def create_new_user(user: schemas.CreateUser, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email_username(db, email=user.email, username=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email and username already registered")
    data = crud.create_new_user(db, user)
    return responses.JSONResponse(content={
        "message":"success",
        "data": {
            "email": data.email,
            "username": data.username
        }
    })


@router.post("/create-user-formdata")
def create_new_user_with_form_data(username: Annotated[str, Form()], email: Annotated[str, Form()]):
    if is_valid_email(email) is False:
        raise HTTPException(status_code=422, detail="Invalid email")
    
    return {
        "username": username,
        "email": email
    }
    
@router.post("/upload-file")
def create_profile_image(uploaded_file: UploadFile):
    file_location = f"files/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    
    return {
        "info": f"file '{uploaded_file.filename}' save at '{file_location}'"
    }
    
@router.get("/{user_id}/allitem", response_model=scm_sqlmodel.UserWithAllItem)
def get_user_with_item(*, session: Session = Depends(get_db), user_id: int):
    data = session.get(sqlm_users.UsersSQM, user_id)
    if not data:
        raise HTTPException(status_code=404, datail="user not found")
    return data


@router.post("/auth/login")
def user_auth_login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    if crud.authenticate_user(db, user.email, user.password) is False:
        return responses.JSONResponse(content={
            "message": "login gagal"
        }, status_code=401)
        
    return responses.JSONResponse(content={
            "message": "login success"
        }, status_code=200)
        