from fastapi import APIRouter
from models.user_schema import UserCreate, UserUpdate, UserResponse, UserListResponse
from controllers import user_controller

router = APIRouter()


@router.get("/users", response_model=UserListResponse, tags=["Users"])
def get_users():
    return user_controller.get_all_users()


@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user_by_id(user_id: str):
    return user_controller.get_user_by_id(user_id)


@router.post("/users", response_model=UserResponse, status_code=201, tags=["Users"])
def create_new_user(user: UserCreate):
    return user_controller.create_new_user(user)


@router.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(user_id: str, updated_user: UserUpdate):
    return user_controller.update_user(user_id, updated_user)


@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: str):
    return user_controller.delete_user(user_id)