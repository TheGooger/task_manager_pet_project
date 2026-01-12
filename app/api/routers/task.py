from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Sequence

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
        owner_id = user.id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get(
    "/",
    response_model=list[TaskPublic],
)
def get_user_tasks(
    is_done: bool | None = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_session),
    user: Users = Depends(get_current_user),
) -> Sequence[Tasks]:
    query = select(Tasks).where(Tasks.owner_id == user.id)
    if is_done is not None:
        query = query.where(Tasks.is_done == is_done)
    query = query.limit(limit).offset(offset)
    return db.scalars(query).all()


@router.get(
    "/{task_id}",
    response_model=TaskPublic,
)
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_session),
    user: Users = Depends(get_current_user),
) -> Tasks:
    task = db.scalar(select(Tasks).where(Tasks.id == task_id, Tasks.owner_id == user.id))
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task
