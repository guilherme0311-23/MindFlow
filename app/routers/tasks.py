from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Task
from app.schemas import Task_Create, TaskResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks", response_model= TaskResponse)
def create_task(task: Task_Create, db: Session = Depends(get_db)):
    nova_task = Task(titulo = task.titulo, descricao=task.descricao)
    db.add(nova_task)
    db.commit()
    db.refresh(nova_task)
    return nova_task

@router.get("/tasks", response_model= list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return task