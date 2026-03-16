async def test_message_valid(client, message_fixture):
    response = client.post("/message", json=message_fixture)
    assert response.status_code == 200


async def test_message_missing_dev_id(client, message_fixture):
    del message_fixture["bizData"]["devId"]

    response = client.post("/message", json=message_fixture)
    assert response.status_code == 422


async def test_message_invalid_code(client, message_fixture):
    message_fixture["bizData"]["properties"][0]["code"] = "bogus"

    response = client.post("/message", json=message_fixture)
    assert response.status_code == 422


async def test_send_valid(client):
    response = client.post("/send", json={"switch": True, "devId": "123"})
    assert response.status_code == 200


async def test_send_invalid(client):
    response = client.post("/send", json={"switch": "Yes please", "devId": "123"})
    assert response.status_code == 422
