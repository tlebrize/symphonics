import asyncio
import pytest
from fastapi.testclient import TestClient

from app import init
from app.database import get_db
from app.schema import migrate, destroy


@pytest.fixture()
def app():
    yield init()


@pytest.fixture()
def client(app):
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def message_fixture():
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


@pytest.fixture(scope="session")
def db_client():
    db = get_db()
    migrate(db)
    yield db
    destroy(db)
