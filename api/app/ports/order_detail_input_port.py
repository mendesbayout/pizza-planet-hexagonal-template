from typing import List, Union

from api.app.adapters.base_adapter import BaseAdapter
from api.app.models.order_detail import OrderDetail
from api.app.use_cases.order_details_use_cases import OrderDetailUseCases


class OrderDetailInputPort:
    def __init__(self, adapter: BaseAdapter) -> None:
        self.order_detail_use_cases = OrderDetailUseCases(adapter)
        super().__init__()

    def get_all(self) -> (List[OrderDetail]):
        return self.order_detail_use_cases.get_all()

    def get_by_id(self, id: str) -> Union[OrderDetail, None]:
        return self.order_detail_use_cases.get_by_id(id)

    def create(self, new_item: dict) -> OrderDetail:
        return self.order_detail_use_cases.create(new_item)

    def update(self, updated_item: dict) -> OrderDetail:
        return self.order_detail_use_cases.update(updated_item)

    def delete(self, _id: int):
        return self.order_detail_use_cases.delete(_id)
