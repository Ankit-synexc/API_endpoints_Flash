from pydantic import BaseModel

class Math(BaseModel):
    operation : str
    a : float
    b : float
    expression : str
    result : float | int