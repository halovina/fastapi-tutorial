from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class CreateUser(UserBase):
    username: str
    
class User(UserBase):
    id: int
    username: str
    
    class Config:
        orm_mode: True