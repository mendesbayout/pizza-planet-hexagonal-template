from typing import List

from fastapi import APIRouter, Response

from api.app.adapters.base_adapter import BaseAdapter
from api.app.models.order_detail import OrderDetail, OrderDetailCreate, OrderDetailUpdate
from api.app.ports.order_detail_input_port import OrderDetailInputPort

order_details = APIRouter()

order_details_port = OrderDetailInputPort(BaseAdapter())


@order_details.get("/", name="get_order_details", response_model=List[OrderDetail])
async def get(response: Response):
    (order_details_response, count) = order_details_port.get_all()
    response.headers["X-Total-Count"] = str(count)
    return order_details_response


@order_details.post("/", name="create_order_detail", status_code=201, response_model=OrderDetail)
async def create_order_detail(order_detail_input: OrderDetailCreate):
    return order_details_port.create(order_detail_input.dict())


@order_details.put("/{order_detail_id}", name="update_order_detail", response_model=OrderDetail)
async def update_order_detail(order_detail_id: str, order_detail_input: OrderDetailUpdate):
    return order_details_port.update({**order_detail_input.dict(), "id": order_detail_id})


@order_details.delete("/{order_detail_id}", status_code=204, name="delete_order_detail")
async def delete_order_detail(order_detail_id: int):
    return order_details_port.delete(order_detail_id)
