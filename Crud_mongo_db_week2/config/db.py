from beanie import init_beanie
from pymongo import AsyncMongoClient

from config.settings import settings
from models.user_schema import User


async def init_db():
    # Use PyMongo's native AsyncMongoClient instead of Motor
    client = AsyncMongoClient(settings.MONGO_URL)

    await init_beanie(
        database=client[settings.DB_NAME],
        document_models=[User]
    )
    print("connected to the database")