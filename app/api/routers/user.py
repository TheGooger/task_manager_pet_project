from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

# from app.api.deps import get_current_user
from app.schemas.user import UserPublic, UserCreate, UserModify
from app.services import user as service
from app.db.session import get_session
from exceptions import Duplicate, Missing


router = APIRouter(prefix="/users", tags=["users"])


# @router.get("/me", response_model=UserPublic)
# def read_me(current_user: Users = Depends(get_current_user)):
#     return current_user


# --- REST API ---

@router.get("/")
def get_all(db: Session=Depends(get_session)) -> list[UserPublic]:
    return service.get_all(db)


@router.get("/{id}")
def get_one(id: int, db: Session=Depends(get_session)) -> UserPublic:
    try:
        return service.get_one(id, db)
    except Missing as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.msg,
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    user: UserCreate,
    db: Session=Depends(get_session)
    ) -> UserPublic:
    try:
        return service.create(user, db)
    except Duplicate as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=e.msg,
        )
    

@router.patch("/")
def modify(
    id: int,
    user: UserModify,
    db: Session=Depends(get_session),
    ) -> UserPublic:
    try:
        return service.modify(id, user, db)
    except Missing as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.msg,
        )
    

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session=Depends(get_session)):
    try:
        service.delete(id, db)
    except Missing as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.msg,
        )
    