from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    BACKEND_URL: str
    DB_DATASET: str
    PUBSUB_TOPIC: str
    DEBUG: bool = True
    TEST: bool = False



class TestSettings:
    BACKEND_URL = "http://localhost:9000"
    DB_DATASET = "test"
    PUBSUB_TOPIC = "test"
    DEBUG = True
    TEST = True


if os.getenv("TEST") == "true":
    settings = TestSettings()
else:
    settings = Settings()  # ty: ignore[missing-argument]
