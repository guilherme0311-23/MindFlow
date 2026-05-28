from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    titulo = Column(String, nullable = False)
    descricao = Column(String, nullable = True)
    concluida = Column(Boolean, default = False)
