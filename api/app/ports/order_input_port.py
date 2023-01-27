from typing import List, Union

from api.app.adapters.base_adapter import BaseAdapter
from api.app.models.order import Order
from api.app.use_cases.order_use_cases import OrderUseCases


class OrderInputPort:
    def __init__(self, adapter: BaseAdapter) -> None:
        self.order_use_cases = OrderUseCases(adapter)
        super().__init__()

    def get_all(self) -> (List[Order]):
        return self.order_use_cases.get_all()

    def get_by_id(self, id: str) -> Union[Order, None]:
        return self.order_use_cases.get_by_id(id)

    def create(self, new_item: dict) -> Order:
        return self.order_use_cases.create(new_item)

    def update(self, updated_item: dict) -> Order:
        return self.order_use_cases.update(updated_item)

    def delete(self, _id: int):
        return self.order_use_cases.delete(_id)
