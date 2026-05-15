from pydantic import BaseModel , Field
from typing import Optional

class Echo(BaseModel):
    message : str = Field(examples=["enter a message"])
    data : Optional[dict] = Field(default = None , examples = [{"key" : "value"}])
class EchoResponse(BaseModel):
    echo_message : str
    echo_data : Optional[dict]

