from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import Settings
from models.user_schema import User

async def init_db():
    client = AsyncIOMotorClient(Settings.MONGO_URL)
    await init_beanie(
        database = client[Settings.DB_NAME],
        document_models= [User]
    )
    print("connected to the database")