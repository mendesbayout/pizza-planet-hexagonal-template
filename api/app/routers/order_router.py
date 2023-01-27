from typing import List, Union

from fastapi import APIRouter, Response

from api.app.adapters.base_adapter import BaseAdapter
from api.app.models.order_detail import OrderDetail
from api.app.ports.order_detail_input_port import OrderDetailInputPort

orders = APIRouter()

orders_port = OrderDetailInputPort(BaseAdapter())


@orders.get("/", name="get_orders", response_model=List[OrderDetail])
async def get(response: Response):
    (orders_response, count) = orders_port.get_all()
    response.headers["X-Total-Count"] = str(count)
    return orders_response


@orders.get("/{order_id}", name="get_order_by_id", response_model=Union[OrderDetail, None])
async def get_by_id(order_id: str):
    return orders_port.get_by_id(order_id)


@orders.post("/", name="create_order", status_code=201, response_model=OrderDetail)
async def create_order(order_input: dict):
    return orders_port.create(order_input)


@orders.put("/{order_id}", name="update_order", response_model=OrderDetail)
async def update_order(order_id: str, order_input: dict):
    order_input["id"] = order_id
    return orders_port.update(order_input)


@orders.delete("/{order_id}", status_code=204, name="delete_order")
async def delete_order(order_id: int):
    return orders_port.delete(order_id)
