from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    ingredient_price: float
    ingredient_id: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int


class OrderDetailUpdate(OrderDetailBase):
    _id: int
    order_id: int


class OrderDetail(OrderDetailBase):
    _id: int
    order_id: int
