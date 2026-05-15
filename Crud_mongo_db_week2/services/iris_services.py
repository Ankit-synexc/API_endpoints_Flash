import numpy as np
from utils.helper import loaded_model
from models.Prediction_log_schema import PredictionLog

SPECIES_MAPPING = {0:"Setosa",1:"Versicolor",2:"Virginica"}

async def perform_prediction(data):
    input_features = np.array([[data.sepal_length,
                                data.sepal_width,
                                data.petal_length,
                                data.petal_width]])

    prediction_index = loaded_model.predict(input_features)[0]
    prediction_name = SPECIES_MAPPING.get(int(prediction_index), "Unknown")

    log_entry = PredictionLog(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction_name
    )
    await log_entry.insert()

    return {
        "prediction_code": int(prediction_index),
        "prediction_name": prediction_name
    }