from pydantic import BaseModel

class Health (BaseModel):
    status : str
    uptime_seconds : float
    timestamp : str
