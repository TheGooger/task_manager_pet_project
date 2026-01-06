from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    

class UserPublic(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True) # Only for ORM -> pydantic


class UserModify(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    is_active: bool | None = None
