from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    BACKEND_URL: str
    DB_DATASET: str
    DEBUG: bool = True
    TEST: bool = False


class TestSettings:
    BACKEND_URL = "http://localhost:9000"
    DB_DATASET = "test"
    DEBUG = True
    TEST = True


if os.getenv("TEST") == "true":
    settings = TestSettings()
else:
    settings = Settings()  # ty: ignore[missing-argument]
