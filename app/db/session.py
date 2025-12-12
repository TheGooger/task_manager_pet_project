from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import get_db_url, settings


DATABASE_URL = get_db_url()
DB_MODE = settings.DB_MODE


# --- Sync setup ---
if DB_MODE.startswith("sync"):
    engine = create_engine(
        DATABASE_URL,
        echo=settings.ECHO,
        future=True # New engine mode, provide select() insert() methods and changes result to tuple
    )
    