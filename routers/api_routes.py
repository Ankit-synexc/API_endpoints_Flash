from fastapi import APIRouter
from routers.health import router as health_router
from routers.echo import router as echo_router
from routers.math import router as math_router
from routers.user import router as user_router

router = APIRouter()

router.include_router(health_router)
router.include_router(echo_router)
router.include_router(math_router)
router.include_router(user_router)
