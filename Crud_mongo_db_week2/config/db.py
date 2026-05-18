from beanie import init_beanie
from pymongo import AsyncMongoClient
from config.settings import settings
from models.user_schema import User
from models.Prediction_log_schema import PredictionLog
from models.session_schema import Session

async def init_db():
    client = AsyncMongoClient(settings.MONGO_URL)

    await init_beanie(
        database=client[settings.DB_NAME],
        document_models=[User, PredictionLog , Session]
    )
    print("connected to the database")