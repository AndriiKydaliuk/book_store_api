def test_get_all(client):
    response = client.get("/user")
    assert response.status_code == 200

