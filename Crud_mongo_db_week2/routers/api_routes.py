from fastapi import APIRouter

from routers.user import router as user_router
from routers.iris import router as iris_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="", tags=["user"])
api_router.include_router(iris_router, prefix="", tags=["iris"])