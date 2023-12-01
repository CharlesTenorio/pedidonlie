from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """Confirutrações gerais usadas na aplicacao"""
    """"""
    API_VERSION: str = '/api/v'
    DB_URL :str = "postgresql+asyncpg://postgres:adm123@localhost:5432/db_loja"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()

