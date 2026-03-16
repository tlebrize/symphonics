async def test_hello(client):
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == "Hello"
