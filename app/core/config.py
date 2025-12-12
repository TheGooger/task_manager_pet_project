from typing import Literal, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database regime, one of:
    DB_MODE: Literal["sync_postgres", "async_postgres", "sync_sqlite", "async_sqlite"] = "sync_sqlite"

    # For Postgres
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "app_db"

    # For sqlite
    SQLITE_FILE_PATH:str = "sqlite.db"

    # Oprionally possible to put URL manually
    DATABASE_URL: Optional[str] = None

    ECHO: bool = False


settings = Settings()

def get_db_url() -> str:
    if settings.DATABASE_URL:
        return settings.DATABASE_URL
    
    mode = settings.DB_MODE

    if mode == "sync_postgres":
        return f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    if mode == "async_postgres":
        return f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    if mode == "sync_sqlite":
        return f"sqlite://{settings.SQLITE_FILE_PATH}"
    if mode == "async_sqlite":
        return f"sqlite+aiosqlite://{settings.SQLITE_FILE_PATH}"
    
    raise RuntimeError(f"Unsupported DB_MODE: {mode}")
    