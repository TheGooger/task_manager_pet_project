from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.services.auth import get_hash
from app.db.models.users import Users
    

def get_user_by_email(db: Session, email: str) -> Users | None:
    return db.scalar(select(Users).where(Users.email == email))


def create_user(db: Session, user_in: UserCreate) -> Users:
    user = Users(
        email=user_in.email,
        password_hash=get_hash(user_in.password),
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user) # for Python object, upload new (id) info from DB
    return user
