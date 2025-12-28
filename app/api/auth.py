from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.schemas.user import UserCreate, UserPublic
from app.crud.user import get_user_by_email, create_user
from app.core.security import verify_password, create_access_token
from app.schemas.token import Token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
)
def register_user(user_in: UserCreate, db: Session = Depends(get_session)):
    user = get_user_by_email(db, user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user = create_user(db, user_in)
    return user


@router.post("/login", response_model=Token)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_session),
):
    user = get_user_by_email(db, form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",)

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",)

    token = create_access_token(str(user.id))

    return Token(access_token=token)
