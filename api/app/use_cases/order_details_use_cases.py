from typing import List, Union

from api.app.adapters.dynamodb.order_detail_adapter import OrderDetailAdapter
from api.app.models.order_detail import OrderDetail, OrderDetailUpdate, OrderDetailCreate
from api.app.utils.exceptions import ItemNotFoundError


class OrderDetailUseCases:
    adapter = OrderDetailAdapter()

    def __init__(self, adapter: OrderDetailAdapter) -> None:
        self.adapter = adapter

    def get_all(self) -> (List[OrderDetail], int):
        return self.adapter.get_all()

    def get_by_id(self, _id: str) -> Union[OrderDetail, None]:
        return self.adapter.get_by_id(_id)

    def create(self, new_item: dict) -> OrderDetail:
        order_detail_to_create = OrderDetailCreate(**new_item)
        (response, order_detail_created) = self.adapter.create(order_detail_to_create.dict())
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return OrderDetail(**order_detail_created, _id=order_detail_created["_id"])
        raise ItemNotFoundError("Error creating order detail")

    def update(self, updated_item: dict) -> OrderDetail:
        exist_order_detail = self.adapter.exist(updated_item.get("_id"))

        if exist_order_detail:
            order_detail = OrderDetailUpdate(**updated_item)
            updated = self.adapter.update(order_detail.dict())
            return OrderDetail(**updated)
        raise ItemNotFoundError("Error updating order detail")

    def delete(self, _id: int):
        return self.adapter.delete(_id)

    def exist(self, _id: int):
        return self.adapter.exist(_id)
