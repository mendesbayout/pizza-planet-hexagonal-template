import urllib.parse
import uuid
from abc import ABC

from app.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter
from app.app.models.ingredient import Ingredient


class IngredientAdapter(DynamoDBAdapter, ABC):
    def __init__(self, pk_identifier="ING", sk_identifier="ING") -> None:
        super().__init__(pk_identifier, sk_identifier)

    def get_all(self):
        ingredient_response = super().get_all()
        parsed_result = [
            Ingredient(**ingredient, id=urllib.parse.quote(f'{ingredient["PK"]}&{ingredient["SK"]}'))
            for ingredient in ingredient_response["Items"]
        ]
        return parsed_result, ingredient_response["Count"]

    def get_by_id(self, item_id: str):
        response = super().get_by_id(item_id)
        if "Item" in response:
            ingredient_response = response["Item"]
            parsed_ingredient = Ingredient(
                **ingredient_response, id=urllib.parse.quote(f'{ingredient_response["PK"]}&{ingredient_response["SK"]}')
            )
            return parsed_ingredient
        return None

    def create(self, new_item: dict):
        var_id = str(uuid.uuid4())
        new_item['PK'] = f"ING#{var_id}"
        new_item['SK'] = f"ING#{var_id}"
        return super().create(new_item)
