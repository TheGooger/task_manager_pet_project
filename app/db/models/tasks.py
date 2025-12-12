from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import Base

if TYPE_CHECKING:
    from .users import Users


class Tasks(Base):
    __name__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    is_done: Mapped[bool] = mapped_column(default=False, server_default=False, index=True)
    created_at: Mapped[DateTime] = mapped_column(default=func.now(), server_default=func.now())

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        )
    owner: Mapped["Users"] = relationship(back_populates="tasks")
