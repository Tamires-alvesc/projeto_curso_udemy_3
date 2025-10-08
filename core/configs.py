from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação"""
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://user_user:password_password@93.188.162.196:5234/faculdade'  #Como fazer usuário e senha do banco de dados ? e como fazer o banco de dados com pgadmin4?
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()