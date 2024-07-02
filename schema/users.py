from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class CreateUser(UserBase):
    password: str
    
class User(UserBase):
    id: int
    username: str
    
    class Config:
        orm_mode: True
        
class UserLogin(UserBase):
    password: str