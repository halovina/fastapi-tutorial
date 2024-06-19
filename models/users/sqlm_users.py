from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class UsersSQM(SQLModel, table=True):
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username : str 
    email : str 
    
    items: list["Item"] = Relationship(back_populates="userItem")
    
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str
    description: str
    price: float
    tax : float | None = None
    user_id : int | None = Field(default=None, foreign_key="users.id")
    
    userItem : UsersSQM | None = Relationship(back_populates="items")
    