from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/")
async def hello():
    return "Hello"
