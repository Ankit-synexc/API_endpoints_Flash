from fastapi import APIRouter
from models.iris_schema import Iris_req
from controllers.iris_controller import get_prediction

router = APIRouter(prefix="/iris", tags=["Classification"])

@router.post("/predict")
async def predict(payload: Iris_req):
    return await get_prediction(payload)