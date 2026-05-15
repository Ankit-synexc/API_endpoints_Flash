from fastapi import HTTPException
from urllib.parse import unquote

# Maps every accepted input to (symbol, function)
OPERATIONS = {
    "add":      ("+",  lambda a, b: a + b),
    "+":        ("+",  lambda a, b: a + b),
    "subtract": ("-",  lambda a, b: a - b),
    "-":        ("-",  lambda a, b: a - b),
    "multiply": ("×",  lambda a, b: a * b),
    "*":        ("×",  lambda a, b: a * b),
    "divide":   ("÷",  lambda a, b: a / b),
    "/":        ("÷",  lambda a, b: a / b),
}


def calculate(operation: str, a: float, b: float) -> dict:

    op = unquote(operation).lower().strip()

    print(f"DEBUG op='{op}' repr={repr(op)}")   

    if op not in OPERATIONS:
        raise HTTPException(
            status_code=400,
            detail={
                "error": f"Unknown operation: '{operation}'",
                "allowed": ["add", "subtract", "multiply", "divide"]
            }
        )

    if op in ("divide", "/") and b == 0:
        raise HTTPException(
            status_code=400,
            detail={"error": "Cannot divide by zero"}
        )

    symbol, func = OPERATIONS[op]
    result = func(a, b)

    return {
        "operation": op,
        "a": a,
        "b": b,
        "expression": f"{a} {symbol} {b}",
        "result": result
    }