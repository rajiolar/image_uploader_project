from sqlalchemy import Column, String, Integer
from model import Base



class User (Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key = True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique = True)
    password = Column(String)
    confirm_password = Column(String)
    profile_picture = Column(String)