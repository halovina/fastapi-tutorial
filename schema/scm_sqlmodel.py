from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username : str
    email: str
    
class UserPublic(UserBase):
    id: int
    
    
class ItemBase(SQLModel):
    name: str
    description: str
    price: float
    tax: float
    
    user_id : int | None = Field(default=None, foreign_key="users.id")
    
class ItemPublic(ItemBase):
    id: int
    
    
class UserWithAllItem(UserPublic):
    items: list[ItemPublic] = []