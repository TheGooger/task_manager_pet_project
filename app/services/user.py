from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserPublic, UserModify
from app.db.data import user as data
from app.core.security import get_hash


def get_all(db: Session) -> list[UserPublic]:
    return data.get_all(db)


def get_one(id: int, db: Session) -> UserPublic:
    return data.get_one(id, db)


def create(user: UserCreate, db: Session) -> UserPublic:
    hash_password = get_hash(user.password)
    return data.create(user.email, hash_password, db)


def modify(id: int, user: UserModify, db: Session) -> UserPublic:
    return data.modify(id, user, db)


def delete(id: int, db: Session):
    return data.delete(id, db)
