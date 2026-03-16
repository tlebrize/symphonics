import asyncio
import pytest
from fastapi.testclient import TestClient

from app import init


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
