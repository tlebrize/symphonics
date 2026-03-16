from enum import Enum
from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.database import get_db
from app.services import MessageService


router = APIRouter()


class PropertyCode(Enum):
    temp_interior = "temp_interior"
    instant_power = "instant_power"


class MessagePropertyModel(BaseModel):
    code: PropertyCode
    dpId: int
    time: int
    value: int


class MessageDataModel(BaseModel):
    devId: str
    dataId: str
    productId: str
    properties: List[MessagePropertyModel]


class MessageModel(BaseModel):
    bizCode: str
    bizData: MessageDataModel
    ts: int


@router.post("/message")
async def message(data: MessageModel, db=Depends(get_db)):
    return MessageService(db).save(data)


class SendModel(BaseModel):
    switch: bool
    devId: str


@router.post("/send")
async def send(data: SendModel):
    return data


@router.get("/report")
async def report() -> dict:
    return {}
