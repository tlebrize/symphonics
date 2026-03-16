from fastapi import APIRouter, Depends

from app.storage import get_db, get_publisher
from app.services import UsageService, DeviceService
from app.models import MessageModel, SendModel

router = APIRouter()


@router.post("/message")
async def message(data: MessageModel, db=Depends(get_db)):
    UsageService(db).save(data.bizData)
    return data


@router.post("/send")
async def send(data: SendModel, publisher=Depends(get_publisher)):
    DeviceService(publisher).switch(switch=data.switch, devId=data.devId)
    return data


@router.get("/report")
async def report(db=Depends(get_db)) -> dict:
    return UsageService(db).report()
