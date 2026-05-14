from fastapi import  HTTPException
from models.user_schema import UserCreate , UserUpdate
from utils.helpers import utc_now , generate_id

users_db : dict [str , dict] = {}

def query_all_users() -> dict:
    return {
        "users" : list(users_db.values()),
        "count" : len(users_db)
    }

def query_create_user(body : UserCreate) -> dict:
    if any(u["email"] == body.email for u in users_db):
        raise HTTPException(status_code=400, detail=f" Email {body.email} already exists!")

    user_id = generate_id()
    user = {
        "id" : user_id,
        "name" : body.name,
        "email" : body.email,
        "age" : body.age,
        "created_at" : utc_now(),

    }
    users_db[user_id] = user
    return user

def query_get_user(user_id) -> dict:
    user = users_db[user_id]
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist!")
    return user

def query_update_user(user_id : str ,body :UserUpdate) -> dict:
    user = users_db[user_id]

    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist!")
    update_data = body.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail = f"No data provided to update the user : {user}",
        )
    user.update(update_data)
    user["updated_at"] = utc_now()
    users_db[user_id] = user
    return user

def query_delete_user(user_id) -> dict:
    user = users_db.pop(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist!")
    return {"message" : f"user with id {user_id} has been deleted!" }

