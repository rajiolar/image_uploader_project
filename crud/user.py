from schema.user import UserCreate
from sqlalchemy.orm import Session
from model.user import User

def create_user ( user:UserCreate, db: Session ):
    
    new_user = User (
    firstname = user.firstname,
    lastname = user.lastname,
    email = user.email,
    password = user.password,
    confirm_password = user.confirm_password,
    profile_picture = user.profile_picture
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def get_user_by_email (user_email: str, db: Session ):
    user = db.query(User).filter_by(email=user_email).first()
    return user