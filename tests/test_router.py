import pytest


@pytest.fixture()
def message():
    return {
        "bizCode": "string",
        "bizData": {
            "devId": "string",
            "dataId": "string",
            "productId": "string",
            "properties": [{"code": "temp_interior", "dpId": 0, "time": 0, "value": 0}],
        },
        "ts": 0,
    }


async def test_message_valid(client, message):
    response = client.post("/message", json=message)
    assert response.status_code == 200


async def test_message_missing_dev_id(client, message):
    del message["bizData"]["devId"]

    response = client.post("/message", json=message)
    assert response.status_code == 422


async def test_message_invalid_code(client, message):
    message["bizData"]["properties"][0]["code"] = "bogus"

    response = client.post("/message", json=message)
    assert response.status_code == 422


async def test_send_valid(client):
    response = client.post("/send", json={"switch": True, "devId": "123"})
    assert response.status_code == 200


async def test_send_invalid(client):
    response = client.post("/send", json={"switch": "Yes please", "devId": "123"})
    assert response.status_code == 422


async def test_report(client):
    response = client.get("/report")
    assert response.status_code == 200
    assert response.json() == {}
