from schema.user import UserCreate
from sqlalchemy.orm import Session
from crud import user as userCrud
from fastapi.exceptions import HTTPException
from fastapi import status

def create_user( user: UserCreate, db: Session):
    
    existing_user = userCrud.get_user_by_email( user.email, db)
    if existing_user:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail="email already exist")
    
    return userCrud.create_user(user, db)  
    