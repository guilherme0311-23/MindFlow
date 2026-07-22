import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base
from app.routers.auth import get_db as get_db_auth
from app.routers.tasks import get_db as get_db_tasks
from app.security import get_db as get_db_security

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_auth] = override_get_db
app.dependency_overrides[get_db_tasks] = override_get_db
app.dependency_overrides[get_db_security] = override_get_db

@pytest.fixture()
def client():

    Base.metadata.create_all(bind=engine)
    yield TestClient(app)

    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def auth_headers(client):
    client.post("/auth/register", json={
        "email": "usuario_tasks@mindflow.com",
        "password": "senha123"
    })

    response = client.post("/auth/login", data={
        "username": "usuario_tasks@mindflow.com",
        "password": "senha123"
    })

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}