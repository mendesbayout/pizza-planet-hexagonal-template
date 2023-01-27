import urllib.parse
import uuid
from abc import ABC

from api.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter
from api.app.models.size import Size


class SizeAdapter(DynamoDBAdapter, ABC):
    def __init__(self, pk_identifier="SIZ", sk_identifier="SIZ") -> None:
        super().__init__(pk_identifier, sk_identifier)

    def get_all(self):
        size_response = super().get_all()
        parsed_result = [
            Size(**size, id=urllib.parse.quote(f'{size["PK"]}&{size["SK"]}'))
            for size in size_response["Items"]
        ]
        return parsed_result, size_response["Count"]

    def get_by_id(self, item_id: str):
        response = super().get_by_id(item_id)
        if "Item" in response:
            size_response = response["Item"]
            parsed_size = Size(
                **size_response, id=urllib.parse.quote(f'{size_response["PK"]}&{size_response["SK"]}')
            )
            return parsed_size
        return None

    def create(self, new_item: dict):
        var_id = str(uuid.uuid4())
        new_item['PK'] = f"SIZ#{var_id}"
        new_item['SK'] = f"SIZ#{var_id}"
        return super().create(new_item)

    def exists(self, item_id: str) -> bool:
        item = self.get_by_id(item_id)
        if item:
            return True
        return False