from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func, true

from .base import Base

if TYPE_CHECKING:
    from .tasks import Tasks


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True, server_default=true())
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=func.now())

    tasks: Mapped[List["Tasks"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
