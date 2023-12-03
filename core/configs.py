from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:supersenha@localhost:5432/db_loja"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()


    