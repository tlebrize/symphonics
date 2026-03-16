from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BACKEND_URL: str
    DEBUG: bool = True


settings = Settings()  # ty: ignore[missing-argument]
