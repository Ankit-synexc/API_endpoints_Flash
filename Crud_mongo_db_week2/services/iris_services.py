import numpy as np
from utils.helper import loaded_model

SPECIES_MAPPING = {0:"Setosa",1:"Versicolor",2:"Virginica"}

def perform_prediction(data):
    input_features = np.array([[data.sepal_length,
                                data.sepal_width,
                                data.petal_length,
                                data.petal_width]])

    prediction_index = loaded_model.predict(input_features)[0]
    return {
        "prediction_code": int(prediction_index),
        "prediction_name": SPECIES_MAPPING.get(int(prediction_index),"Unknown")


    }