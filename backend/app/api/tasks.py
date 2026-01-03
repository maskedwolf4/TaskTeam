from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.core.auth import *
from app.models.tasks import Task
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate, TaskStatusUpdate

router = APIRouter(
    prefix="/api/tasks",
    tags=["tasks"]
)

@router.get("/", response_model=List[TaskResponse])
def list_tasks(
    user: AuthUser = Depends(require_view),
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).filter(Task.org_id == user.org_id).all()
    return tasks

@router.post("/", response_model=TaskResponse)
def create_tasks(
    task_in: TaskCreate,
    user: AuthUser = Depends(require_create),
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task_in.title,
        description=task_in.description,
        org_id=user.org_id,
        created_by=user.user_id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: str,
    user: AuthUser = Depends(require_view),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, 
                                 Task.org_id == user.org_id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    task_in: TaskUpdate,
    user: AuthUser = Depends(require_edit),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, 
                                 Task.org_id == user.org_id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    if task_in.status is not None:
        task.status = task_in.status
    if task_in.title is not None:
        task.title = task_in.title
    if task_in.description is not None:
        task.description = task_in.description
        
    db.commit()
    db.refresh(task)
    
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: str,
    user: AuthUser = Depends(require_delete),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, 
                                 Task.org_id == user.org_id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return None