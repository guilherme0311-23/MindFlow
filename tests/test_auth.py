def test_register_success(client):
    response = client.post("/auth/register", json = {
        "email": "teste1@mindflow.com",
        "password": "senha123"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "teste1@mindflow.com"
    assert "id" in data

def test_register_duplicate_email(client):
    client.post("/auth/register", json={
        "email": "duplicado@mindflow.com",
        "password": "senha123"
    })
    response = client.post("/auth/register", json={
     "email": "duplicado@mindflow.com",
     "password": "outrasenha"   
    })

    assert response.status_code == 400

def test_login_success(client):
    client.post("/auth/register", json={
        "email": "login@mindflow.com",
        "password": "senha123"
    })

    response = client.post("/auth/login", data={
        "username": "login@mindflow.com",
        "password": "senha123"
    })

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "senhaerrada@mindflow.com",
        "password": "senhacerta"
    })

    response = client.post("/auth/login", data={
        "username": "senhaerrada@mindflow.com",
        "password": "senhaerradaaqui"
    })

    assert response.status_code == 401