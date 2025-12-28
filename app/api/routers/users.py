from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.schemas.user import UserPublic
from app.db.models.users import Users


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserPublic)
def read_me(current_user: Users = Depends(get_current_user)):
    return current_user