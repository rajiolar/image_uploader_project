from pydantic import BaseModel

class UserCreate (BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    confirm_password : str
    profile_picture: str
    
class SignupResponse (BaseModel):
    firstname: str
    lastname: str
    email: str
    