from fastapi import APIRouter , Depends
from models.iris_schema import Iris_req
from controllers.iris_controller import get_prediction
from utils.dependencies import get_current_active_user
from models.user_schema import User

router = APIRouter(prefix="/iris")

@router.post("/predict")
async def predict(
        payload: Iris_req,
        current_user : User = Depends(get_current_active_user),
):

    return await get_prediction(payload, user_id = current_user.id)