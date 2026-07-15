from pydantic import BaseModel
from typing import Optional

class Task_Create(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao : Optional[str] = None
    concluida: bool
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True