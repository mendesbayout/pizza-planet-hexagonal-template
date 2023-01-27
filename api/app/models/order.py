from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

from api.app.models.order_detail import OrderDetail
from api.app.models.size import Size


class OrderBase(BaseModel):
    client_name: str
    client_dni: str
    client_address: str
    client_phone: str
    date: datetime = datetime.utcnow()
    total_price: float
    size_id: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    _id: int


class Order(OrderBase):
    _id: int
    size: Union[Size, None] = None
    detail: Union[List[OrderDetail], None] = None
