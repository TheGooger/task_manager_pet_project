from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserPublic, UserModify


def get_all(db: Session) -> list[UserPublic]:
    


# def get_user_by_email(db: Session, email: str) -> Users | None:
#     return db.query(Users).filter(Users.email == email).first()


# def create_user(db: Session, user_in: UserCreate) -> Users:
#     user = Users(
#         email=user_in.email,
#         password_hash=get_hash(user_in.password),
#         is_active=True,
#     )

#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
