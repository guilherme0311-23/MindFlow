def test_ownership_isolation(client):
    client.post("/auth/register", json={
        "email": "usuarioA@mindflow.com",
        "password": "senha123"
    })
    login_a = client.post("/auth/login", data={
        "username" : "usuarioA@mindflow.com",
        "password": "senha123"
    })
    token_a = login_a.json()["access_token"]
    headers_a = {"Authorization": f"Bearer {token_a}"}

    create_response = client.post("/tasks", json={
        "titulo": "Task privada do usuário A",
        "descricao": "Ninguém mais deveria ver isso"
    }, headers=headers_a)
    task_id = create_response.json()["id"]

    client.post("/auth/register", json={
        "email": "usuarioB@mindflow.com",
        "password": "senha123"
    })
    login_b = client.post("/auth/login", data={
        "username" : "usuarioB@mindflow.com",
        "password": "senha123"
    })
    token_b = login_b.json()["access_token"]
    headers_b = {"Authorization": f"Bearer {token_b}"}

    response = client.get(f"/tasks/{task_id}", headers=headers_b)
    assert response.status_code == 404

    response = client.patch(f"/tasks/{task_id}", json={
        "titulo": "tentativa de invasão"
    }, headers=headers_b)
    assert response.status_code == 404

    response = client.delete(f"/tasks/{task_id}", headers=headers_b)
    assert response.status_code == 404