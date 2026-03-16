import asyncio
import pytest
from fastapi.testclient import TestClient

from app import init
from app.storage import get_db, get_publisher
from app.schema import migrate, destroy
from app.services import UsageService, DeviceService


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


@pytest.fixture(scope="session", autouse=True)
def db_client():
    db = get_db()
    migrate(db)
    yield db
    destroy(db)

@pytest.fixture()
def usage_service(db_client):
    return UsageService(db_client)

@pytest.fixture(scope="session", autouse=True)
def publisher_client():
    return get_publisher()

@pytest.fixture()
def device_service(publisher_client):
    return DeviceService(publisher_client)