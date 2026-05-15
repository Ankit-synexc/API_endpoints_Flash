from datetime import datetime
from beanie import PydanticObjectId
from models.user_schema import User, CreateUser
from typing import List, Optional

async def create_user(payload: CreateUser) -> User:
    user = User(**payload.model_dump())
    await user.insert()
    return user

async def get_all_users() -> List[User]:
    return await User.find().to_list()

async def get_user_by_id(user_id: PydanticObjectId) -> Optional[User]:
    return await User.get(user_id)

async def update_user(user: User, updates: dict) -> User:
    # Set the dictionary of updates to the database document
    await user.set(updates)
    return user

async def delete_user(user: User) -> None:
    await user.delete()

async def db_get_user_by_email(email: str) -> Optional[User]:
    return await User.find_one(User.email == email)