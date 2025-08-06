# FastApi

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model for Todo
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory Todo List
todo_list: List[Todo] = []

# Class-based Todo CRUD
class TodoAPI:

    @staticmethod
    @app.post("/todos/", response_model=Todo)
    def create_todo(todo: Todo):
        # Check for duplicate ID
        for existing in todo_list:
            if existing.id == todo.id:
                raise HTTPException(status_code=400, detail="Todo with this ID already exists.")
        todo_list.append(todo)
        return todo

    @staticmethod
    @app.get("/todos/", response_model=List[Todo])
    def get_all_todos():
        return todo_list

    @staticmethod
    @app.get("/todos/{todo_id}", response_model=Todo)
    def get_todo(todo_id: int):
        for todo in todo_list:
            if todo.id == todo_id:
                return todo
        raise HTTPException(status_code=404, detail="Todo not found.")

    @staticmethod
    @app.put("/todos/{todo_id}", response_model=Todo)
    def update_todo(todo_id: int, updated_todo: Todo):
        for index, todo in enumerate(todo_list):
            if todo.id == todo_id:
                todo_list[index] = updated_todo
                return updated_todo
        raise HTTPException(status_code=404, detail="Todo not found.")

    @staticmethod
    @app.delete("/todos/{todo_id}")
    def delete_todo(todo_id: int):
        for index, todo in enumerate(todo_list):
            if todo.id == todo_id:
                del todo_list[index]
                return {"message": "Todo deleted successfully."}
        raise HTTPException(status_code=404, detail="Todo not found.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
