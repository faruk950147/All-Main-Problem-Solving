from typing import List
from fastapi import HTTPException
from models.tasks import Task

class TasksService:
    task_list: List[Task] = []

    @classmethod
    def create_task(cls, task: Task) -> Task:
        for existing in cls.task_list:
            if existing.id == task.id:
                raise HTTPException(status_code=400, detail="Task with this ID already exists.")
        cls.task_list.append(task)
        return task

    @classmethod
    def get_all_tasks(cls) -> List[Task]:
        return cls.task_list

    @classmethod
    def get_task(cls, task_id: int) -> Task:
        for task in cls.task_list:
            if task.id == task_id:
                return task
        raise HTTPException(status_code=404, detail="Task not found.")

    @classmethod
    def update_task(cls, task_id: int, updated_task: Task) -> Task:
        for index, task in enumerate(cls.task_list):
            if task.id == task_id:
                cls.task_list[index] = updated_task
                return updated_task
        raise HTTPException(status_code=404, detail="Task not found.")

    @classmethod
    def delete_task(cls, task_id: int) -> dict:
        for index, task in enumerate(cls.task_list):
            if task.id == task_id:
                del cls.task_list[index]
                return {"message": "Task deleted successfully."}
        raise HTTPException(status_code=404, detail="Task not found.")
