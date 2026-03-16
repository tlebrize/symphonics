from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import router
from app.settings import settings


def init():
    server = FastAPI(title="Symphonics")

    server.add_middleware(
        CORSMiddleware,  # ty: ignore[invalid-argument-type]
        allow_origins=[settings.BACKEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.include_router(router)

    return server
