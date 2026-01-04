from typing import Generator, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import get_db_url, settings
from .models import Base


DATABASE_URL = get_db_url()


# ---Async setup---
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


async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
