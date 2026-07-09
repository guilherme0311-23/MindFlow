from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    titulo = Column(String, nullable = False)
    descricao = Column(String, nullable = True)
    concluida = Column(Boolean, default = False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index=True)
    email = Column(String, unique= True)
    hashed_password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow)