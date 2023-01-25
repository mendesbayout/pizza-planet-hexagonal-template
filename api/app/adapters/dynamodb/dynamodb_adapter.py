import boto3
from boto3.dynamodb.conditions import Attr

from app.app.adapters.base_adapter import BaseAdapter


class DynamoDBAdapter(BaseAdapter):
    def __init__(self, pk_identifier, sk_identifier):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table("pizza-plannet")
        self.pk_identifier = pk_identifier
        self.sk_identifier = sk_identifier or pk_identifier

    def get_all(self):
        result = self.table.scan(
            FilterExpression=Attr("PK").begins_with(self.pk_identifier) & Attr("SK").begins_with(self.sk_identifier)
        )
        return result

    def get_by_field(self, field, value):
        result = self.table.scan(
            FilterExpression=Attr("PK").begins_with(self.pk_identifier)
                             & Attr("SK").begins_with(self.sk_identifier)
                             & Attr(field).eq(value)
        )
        return result

    def get_by_id(self, item_id: str):
        [pk, sk] = item_id.split("&")
        result = self.table.get_item(Key={"PK": pk, "SK": sk})
        return result

    def get_by_partition_key(self, partition_key: str):
        result = self.table.scan(
            FilterExpression=Attr("PK").eq(partition_key) & Attr("SK").begins_with(self.sk_identifier)
        )
        return result

    def create(self, new_item: dict):
        result = self.table.put_item(Item=new_item)
        return result, new_item

    def delete(self, item_id: int):
        self.table.delete_item(Key={"id": item_id})

    def update(self, updated_item: dict):
        self.table.update_item(
            Key={"id": updated_item["id"]},
            UpdateExpression="SET field1 = :val1, field2 = :val2",
            ExpressionAttributeValues={
                ":val1": updated_item["field1"],
                ":val2": updated_item["field2"],
            },
        )
