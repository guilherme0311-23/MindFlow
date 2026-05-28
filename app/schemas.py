from pydantic import BaseModel
from typing import Optional

class Task_Create(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao : Optional[str] = None
    concluida: bool
    
    class Config:
        from_attributes = True