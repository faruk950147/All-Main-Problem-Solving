from fastapi import APIRouter
from typing import List
from models.tasks import Task
from services.service import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post("/", response_model=Task)
def create_task(task: Task):
    return TasksService.create_task(task)

@router.get("/", response_model=List[Task])
def get_all_tasks():
    return TasksService.get_all_tasks()

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    return TasksService.get_task(task_id)

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    return TasksService.update_task(task_id, updated_task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    return TasksService.delete_task(task_id)
