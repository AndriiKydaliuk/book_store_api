def test_001(client):
    response = client.get("/user")
    assert response.status_code == 200
