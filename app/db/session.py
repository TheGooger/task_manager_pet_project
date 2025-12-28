from typing import Generator, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import get_db_url, settings


DATABASE_URL = get_db_url()
DB_MODE = settings.DB_MODE


# --- Sync setup ---
if DB_MODE.startswith("sync"):
    engine = create_engine(
        DATABASE_URL,
        echo=settings.ECHO,
    )
    SessionLocal = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        autoflush=False,
        )
    

    def get_session() -> Generator[Session, None, None]:
        """Sync dependency - yield DB Session"""
        with SessionLocal() as session:
            yield session


# ---Async setup---
elif DB_MODE.startswith("async"):
    # create async engine 
    async_engine = create_async_engine(
        DATABASE_URL,
        echo=settings.ECHO,
        )
    AsyncSessionLocal = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )

    async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
        """Async dependency - yield AsyncSession"""
        async with AsyncSessionLocal() as session:
            yield session


else:
    raise RuntimeError(f"Unknown DB_MODE: {DB_MODE}")
