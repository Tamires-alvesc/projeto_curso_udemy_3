from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import List

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação"""
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://user_user:password_password@93.188.162.196:5234/faculdade'  #Como fazer usuário e senha do banco de dados ? e como fazer o banco de dados com pgadmin4?
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'yaPVNM4dRdRQ6Sif1CuDF12KW7f7Lx5jCBloBTDoUOg'

    """
    Token gerado com: python3 -c "import secrets; print(secrets.token_urlsafe(32))"
    Ou use o script: python3 gerar_token.py
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7   # 7 days

    class Config:
        case_sensitive = True   


settings: Settings = Settings()