from typing import Annotated
from fastapi import APIRouter , Query
from models.math_schema import Math
from controllers import math_controller

router = APIRouter()

@router.get('/math',response_model=Math)
def math(
        operation : Annotated[str , Query(description = "add | subtract | multiply | divide")],
        a :Annotated[float , Query(description = "First number")],
        b :Annotated[float , Query(description = "Second number")],
):
    return math_controller.simple_math(operation,a,b)

