from datetime import datetime

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, false
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import Base

if TYPE_CHECKING:
    from .users import Users


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    is_done: Mapped[bool] = mapped_column(default=False, server_default=false(), index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(),
        server_default=func.now(),
        onupdate=func.now,
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        )
    owner: Mapped["Users"] = relationship(back_populates="tasks")
