from fastapi import FastAPI
from app.routers import tasks
from app.routers import auth
from app.database import engine
from app import models

app = FastAPI()

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}