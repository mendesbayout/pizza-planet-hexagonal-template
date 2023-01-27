from typing import List, Union

from api.app.adapters.base_adapter import BaseAdapter
from api.app.models.size import Size
from api.app.use_cases.size_use_cases import SizeUseCases


class SizeInputPort:
    def __init__(self, adapter: BaseAdapter) -> None:
        self.size_use_cases = SizeUseCases(adapter)
        super().__init__()

    def get_all(self) -> (List[Size]):
        return self.size_use_cases.get_all()

    def get_by_id(self, id: str) -> Union[Size, None]:
        return self.size_use_cases.get_by_id(id)

    def create(self, new_item: dict) -> Size:
        return self.size_use_cases.create(new_item)

    def update(self, updated_item: dict) -> Size:
        return self.size_use_cases.update(updated_item)

    def delete(self, _id: int):
        return self.size_use_cases.delete(_id)
