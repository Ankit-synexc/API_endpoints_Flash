from utils.helper import loaded_model
from services import iris_services , prediction_log_services

from fastapi import HTTPException


async def get_prediction(payload):

    try:
        result  = iris_services.perform_prediction(payload)
        return {
            "status" : "success",
            "prediction" : result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    iris_services.predict_iris(payload)
