from beanie import PydanticObjectId , Document
from pydantic import Field
from datetime import datetime , timezone

class Session(Document):
    user_id : str
    status : str = "active"
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "sessions"