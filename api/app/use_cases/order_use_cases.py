from typing import List, Union

from app.app.adapters.base_adapter import BaseAdapter
from app.app.adapters.dynamodb.orderAdapter import OrderAdapter
from app.app.models.order import Order, OrderCreate, OrderUpdate
from app.app.utils.exceptions import ItemNotFoundError


class OrderUseCases:
    order_adapter = OrderAdapter()
    adapter = BaseAdapter()

    def __init__(self, adapter: BaseAdapter) -> None:
        self.adapter = adapter

    def get_all(self) -> (List[Order], int):
        return self.adapter.get_all()

    def get_by_id(self, id: int) -> Union[Order, None]:
        return self.adapter.get_by_id(id)

    def create(self, new_item: dict) -> Order:
        order_to_create = OrderCreate(**new_item)
        (response, order_created) = self.adapter.create(order_to_create.dict())
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return Order(**order_created, id=f"{order_created['PK']}&{order_created['SK']}")
        raise ItemNotFoundError("Error creating order")

    def update(self, updated_item: dict) -> Order:
        exist_order = self.order_adapter.exist(item_id=updated_item.get("_id", 0))

        if exist_order:
            order = OrderUpdate(**updated_item)
            updated = self.adapter.update(order.dict())
            return Order(**updated)
        raise ItemNotFoundError("Error updating order")

    def delete(self, _id: int):
        return self.adapter.delete(_id)

    def exist(self, _id: int):
        return self.adapter.exist(_id)
