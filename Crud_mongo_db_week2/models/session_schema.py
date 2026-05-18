from datetime import datetime

from beanie import Document
from pydantic import Field


class Session(Document):
    user_id : str
    status : str = "active"
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "sessions"