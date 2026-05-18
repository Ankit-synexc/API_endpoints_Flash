from fastapi import APIRouter , Depends
from typing import List
from beanie import PydanticObjectId
from controllers import user_controller

from models import user_schema
from utils.dependencies import get_current_active_user
from models.user_schema import User

router = APIRouter()

@router.post('/users', response_model=user_schema.UserResponse)
async def route_create_user(payload: user_schema.CreateUser):
    return await user_controller.create_user(payload)

@router.get('/users' , response_model=List[user_schema.UserResponse])
async def route_get_users(current_users: User = Depends(get_current_active_user)):
    return await user_controller.get_all_users()

@router.get('/users/{user_id}', response_model=user_schema.UserResponse)
async def route_get_user_by_id(
        user_id: PydanticObjectId,
        current_user: User = Depends(get_current_active_user)
        ):
    return await user_controller.get_user_by_id(user_id)

@router.patch('/users/{user_id}' , response_model = user_schema.UserResponse)
async def route_update_user(user_id: PydanticObjectId, payload: user_schema.UserUpdate , current_user: User = Depends(get_current_active_user)):
    return await user_controller.update_user(user_id, payload)

@router.delete('/users/{user_id}')
async def route_delete_user(user_id: PydanticObjectId , current_user: User = Depends(get_current_active_user)):
    return await user_controller.delete_user(user_id)