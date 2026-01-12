from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.schemas.task import TaskPublic, TaskCreate
from app.api.deps import get_current_user
from app.db.models.users import Users
from app.db.models.tasks import Tasks


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "/",
    response_model=TaskPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    new_task: TaskCreate, 
    db: Session = Depends(get_session),
    user: Users = Depends(get_current_user),
) -> Tasks | None:
    if not new_task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    task = Tasks(
        title = new_task.title,
        description = new_task.description,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
    