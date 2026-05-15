from typing import List
from beanie import PydanticObjectId
from fastapi import HTTPException ,status

from models.user_schema import CreateUser , UserResponse , UserUpdate

from services import user_services
from services.user_services import db_get_user_by_email


def _serializer(user) -> UserResponse:
    return UserResponse(
        id = str(user.id),
        name = user.name,
        email = user.email,
        age = user.age,
    )

async def create_user(payload: CreateUser) -> UserResponse:
    existing = await db_get_user_by_email(payload.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Email already registered")
    user = await user_services.create_user(payload)
    return _serializer(user)

async def get_all_users() -> List[UserResponse]:
    users = await user_services.get_all_users()
    return [_serializer(user) for user in users]

async def get_user_by_id(user_id: PydanticObjectId) -> UserResponse:
    user = await user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = "User not found")
    return _serializer(user)

async def update_user(userid : PydanticObjectId, payload: UserUpdate) -> UserResponse:
    user = await user_services.get_user_by_id(userid)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "No updates found")
    user = await user_services.update_user(user, updates)
    return _serializer(user)

async def delete_user(user_id: PydanticObjectId) -> dict:
    user = await user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    await user_services.delete_user(user)
    return {"detail": "User successfully deleted"}