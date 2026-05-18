from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from beanie import Document, Indexed

class User(Document):
    name: str
    email: Indexed(EmailStr, unique=True)
    age: Optional[int]
    password: str

    class Settings:
        name = "users"
        user_state_management = True

class CreateUser(BaseModel):
    name: str = Field
    email: EmailStr
    age: Optional[int] = None
    password: str = Field

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: Optional[int]
    model_config = {"from_attributes": True}