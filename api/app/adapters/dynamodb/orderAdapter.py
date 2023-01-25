import urllib.parse
import uuid

from app.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter
from app.app.models.order import Order


class OrderAdapter(DynamoDBAdapter):
    def __init__(self, pk_identifier="ORD", sk_identifier="ORD") -> None:
        super().__init__(pk_identifier, sk_identifier)

    def get_all(self):
        order_response = super().get_all()
        parsed_result = [
            Order(**order, id=urllib.parse.quote(f'{order["PK"]}&{order["SK"]}'))
            for order in order_response["Items"]
        ]
        return parsed_result, order_response["Count"]

    def get_by_id(self, item_id: str):
        response = super().get_by_id(item_id)
        if "Item" in response:
            order_response = response["Item"]
            parsed_order = Order(
                **order_response, id=urllib.parse.quote(f'{order_response["PK"]}&{order_response["SK"]}')
            )
            return parsed_order
        return None

    def create(self, new_item: dict):
        var_id = str(uuid.uuid4())
        new_item['PK'] = f"ORD#{var_id}"
        new_item['SK'] = f"ORD#{var_id}"
        return super().create(new_item)
