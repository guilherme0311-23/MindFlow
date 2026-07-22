def test_create_task(client, auth_headers):
    response = client.post("/tasks", json={
        "titulo": "Estudar FastAPI",
        "descricao": "Revisar dependency injection"
    }, headers = auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Estudar FastAPI"
    assert data["concluida"] == False

def test_get_tasks(client, auth_headers):

    create_response = client.post("/tasks", json={
        "titulo": "Estudar FastAPI",
        "descricao": "Revisar dependency injection"
    }, headers=auth_headers)

    response = client.get("/tasks", headers = auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

def test_update_task(client, auth_headers):
    create_response = client.post("/tasks", json={
        "titulo": "Titulo original",
        "descricao": "Descricao original"
    }, headers=auth_headers)

    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={
        "titulo": "Titulo atualizado"
    }, headers=auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Titulo atualizado"

def test_delete_task(client, auth_headers):
    create_response = client.post("/tasks", json={
        "titulo": "Task pra deletar",
        "descricao": None
    }, headers=auth_headers)

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=auth_headers)

    assert response.status_code == 204