import urllib.parse
import uuid
from abc import ABC

from api.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter
from api.app.models.order_detail import OrderDetail


class OrderDetailAdapter(DynamoDBAdapter, ABC):
    def __init__(self, pk_identifier="ORD", sk_identifier="DET") -> None:
        super().__init__(pk_identifier, sk_identifier)

    def get_all(self):
        order_detail_response = super().get_all()
        parsed_result = [
            OrderDetail(**order_detail, id=urllib.parse.quote(f'{order_detail["PK"]}&{order_detail["SK"]}'))
            for order_detail in order_detail_response["Items"]
        ]
        return parsed_result, order_detail_response["Count"]

    def get_by_id(self, item_id: str):
        response = super().get_by_id(item_id)
        if "Item" in response:
            order_detail_response = response["Item"]
            parsed_order_detail = OrderDetail(
                **order_detail_response,
                id=urllib.parse.quote(f'{order_detail_response["PK"]}&{order_detail_response["SK"]}')
            )
            return parsed_order_detail
        return None

    def create(self, new_item: dict):
        var_id = str(uuid.uuid4())
        new_item['PK'] = f"ORD#{var_id}"
        new_item['SK'] = f"DET#{var_id}"
        return super().create(new_item)

    def update(self, updated_item: dict):
        response = super().update(updated_item)
        if "Attributes" in response:
            order_detail_response = response["Attributes"]
            parsed_order_detail = OrderDetail(
                **order_detail_response,
                id=urllib.parse.quote(f'{order_detail_response["PK"]}&{order_detail_response["SK"]}')
            )
            return parsed_order_detail
        return None

    def exists(self, item_id: str) -> bool:
        item = self.get_by_id(item_id)
        if item:
            return True
        return False