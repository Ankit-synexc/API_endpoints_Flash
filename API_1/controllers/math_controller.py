from services import math_services

def simple_math(operation : str , a : float, b : float):
    return math_services.calculate(operation, a, b)