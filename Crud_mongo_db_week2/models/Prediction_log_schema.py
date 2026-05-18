from beanie import Document, PydanticObjectId
from datetime import datetime
from pydantic import Field
from typing import Optional

class PredictionLog(Document):
    user_id : Optional[PydanticObjectId] = None
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    prediction : str
    model_version : str =  "knn_v1"
    timestamp : datetime = Field(default_factory=datetime.now)