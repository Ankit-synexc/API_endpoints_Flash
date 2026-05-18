from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URL : str
    DB_NAME : str = "Crud_mongo_db_week2"
    SECRET_KEY : str
    ALGORITHM : str = "HS256"

    model_config = SettingsConfigDict(env_file = ".env" , env_file_encoding = "utf-8")


# noinspection PyArgumentList
settings = Settings()