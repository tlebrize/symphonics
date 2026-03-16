from enum import Enum
from typing import List
from pydantic import BaseModel


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


class SendModel(BaseModel):
    switch: bool
    devId: str
