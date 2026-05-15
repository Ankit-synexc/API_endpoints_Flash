from pydantic import BaseModel

class Iris_req(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    