from typing import List, Union

from app.app.adapters.base_adapter import BaseAdapter
from app.app.models.order_detail import OrderDetail
from app.app.use_cases.order_detail_use_cases import OrderDetailUseCases


class OrderDetailInputPort:
    def __init__(self, adapter: BaseAdapter) -> None:
        self.order_detail_use_cases = OrderDetailUseCases(adapter)
        super().__init__()

    def get_all(self) -> (List[OrderDetail], int):
        return self.order_detail_use_cases.get_all()

    def get_by_id(self, id: str) -> Union[OrderDetail, None]:
        return self.order_detail_use_cases.get_by_id(id)

    def create(self, new_item: dict) -> OrderDetail:
        return self.order_detail_use_cases.create(new_item)

    def update(self, updated_item: dict) -> OrderDetail:
        return self.order_detail_use_cases.update(updated_item)

    def delete(self, _id: int):
        return self.order_detail_use_cases.delete(_id)
