from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Banco de dados fake - lista em memória
tasks_db = []
task_counter = 1

#Schema de entrada - o que o usuário manda
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema de saida - o que a API devolve
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

@router.post("/tasks", response_model= Task)
def create_task(task: TaskCreate):
    global task_counter
    new_task = Task(id=task_counter, title=task.title, description=task.description)
    tasks_db.append(new_task)
    task_counter += 1
    return new_task

@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks_db

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Task not found")