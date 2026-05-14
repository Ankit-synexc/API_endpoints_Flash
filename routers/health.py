from fastapi import APIRouter
from models.health_schema import Health
from controllers import health_controller

router = APIRouter()


@router.get('/health' , response_model=Health)
def health():
    return health_controller.get_health()



