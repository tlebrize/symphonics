from fastapi import APIRouter, Depends

from app.database import get_db
from app.services import UsageService
from app.models import MessageModel, SendModel

router = APIRouter()


@router.post("/message")
async def message(data: MessageModel, db=Depends(get_db)):
    return UsageService(db).save(data.bizData)


@router.post("/send")
async def send(data: SendModel):
    return data


@router.get("/report")
async def report() -> dict:
    return {}
