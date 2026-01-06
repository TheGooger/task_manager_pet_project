from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings


engine = create_engine(
    settings.DB_URL,
    echo=settings.ECHO,
    future=True,
    )

SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
    autoflush=False,
)

def get_session() -> Generator[Session, None, None]:
    """sync dependency - yield Session"""
    with SessionLocal() as session:
        yield session
