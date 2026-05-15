from beanie import Document
from datetime import datetime
from pydantic import Field

class PredictionLog(Document):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    prediction : str
    model_version = "knn_v1"
    timestamp : datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "Prediction Log"
