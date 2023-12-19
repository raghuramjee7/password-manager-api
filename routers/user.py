from typing import Optional, List
from fastapi import Depends, FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session
from database import model
from database.pydantic_models import UserIn
from fastapi import APIRouter
from database.connect import get_db
from utils.auth_util import pwd_context, hash_password

router = APIRouter(
    prefix="/users",
    tags = ['Users']
)

def username_conditions(username: str, db):

    if len(username) < 4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username must be at least 4 characters long")

    if db.query(model.User).filter(model.User.username == username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

def password_conditions(password: str):
    
    if len(password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be at least 8 characters long")
    
    if not any([char not in '0123456789' for char in password]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one number")
    
    if not any([char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for char in password]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one uppercase letter")
    
    if not any([char not in 'abcdefghijklmnopqrstuvwxyz' for char in password]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one lowercase letter")
    
    if not any([char not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in password]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one special character")
    

@router.post("/", status_code = status.HTTP_201_CREATED)
async def create_user(user: UserIn, db: Session = Depends(get_db)):

    username_conditions(user.username, db)
    password_conditions(user.password)

    user.password = hash_password(user.password)
    new_user = model.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Succesfully Created"
    }