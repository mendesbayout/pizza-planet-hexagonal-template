from typing import List, Union

from api.app.adapters.dynamodb.sizeAdapter import SizeAdapter
from api.app.models.size import Size, SizeUpdate, SizeCreate
from api.app.utils.exceptions import ItemNotFoundError


class SizeUseCases:
    size_adapter = SizeAdapter()

    def get_all(self) -> (List[Size], int):
        return self.size_adapter.get_all()

    def get_by_id(self, _id: str) -> Union[Size, None]:
        return self.size_adapter.get_by_id(_id)

    def create(self, new_item: dict) -> Size:
        size_to_create = SizeCreate(**new_item)
        (response, size_created) = self.size_adapter.create(size_to_create.dict())
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return Size(**size_created, id=f"{size_created['PK']}&{size_created['SK']}")
        raise ItemNotFoundError("Error creating size")

    def update(self, updated_item: dict) -> Size:
        exist_size = self.size_adapter.exist(item_id=updated_item.get("_id", 0))
        if exist_size:
            size = SizeUpdate(**updated_item)
            updated = self.size_adapter.update(size.dict())
            return Size(**updated)
        raise ItemNotFoundError("Error updating size")

    def delete(self, _id: int):
        return self.size_adapter.delete(_id)

    def exist(self, _id: int):
        return self.size_adapter.exist(_id)
