from models.user_schema import UserCreate , UserUpdate
from services import user_services

def get_all_users():
    return user_services.query_all_users()


def get_user_by_id(user_id : str):
    return user_services.query_get_user(user_id)

def create_new_user(user : UserCreate):
    return user_services.query_create_user(user)

def update_user(user_id:str ,updated_user : UserUpdate):
    return user_services.query_update_user(user_id , updated_user)

def delete_user(user_id: str):
    return user_services.query_delete_user(user_id)