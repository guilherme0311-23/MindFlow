from fastapi import FastAPI
from app.routers import tasks
from app.database import engine
from app import models

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(tasks.router)

@app.get("/health")

def health_check():
    return {"status": "ok"}