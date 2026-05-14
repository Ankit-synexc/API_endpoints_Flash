from pydantic import BaseModel , Field  , EmailStr
from typing import Optional , Annotated

class UserCreate(BaseModel):
    name: Annotated[str , Field(min_length=1 , max_length=255 , examples=["Alice"])]
    email: EmailStr
    age : Annotated[Optional[int] , Field(default=None , gt=1 , examples = [30])]

class UserUpdate(BaseModel):
    name : Annotated[Optional[str],Field(default=None,min_length=1,max_length=255)]
    email : Optional[EmailStr] = None
    age : Annotated[Optional[int] , Field(default= None , gt = 1)]

class UserResponse(BaseModel):
    id : str
    name : str
    email : str
    age : Optional[int]
    created_at : str
    updated_at : Optional[str] = None

class UserListResponse(BaseModel):
    users : list[UserResponse]
    count: int


