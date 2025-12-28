from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=20)
    description: str | None = None


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=20)
    description: Optional[str] = None
    is_done: Optional[bool] = None


class TaskPublic(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    owner_id: int
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
