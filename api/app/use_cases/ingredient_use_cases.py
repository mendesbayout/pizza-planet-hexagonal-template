from typing import List, Union

from app.app.adapters.base_adapter import BaseAdapter
from app.app.adapters.dynamodb.ingredientAdapter import IngredientAdapter
from app.app.models.ingredient import Ingredient, IngredientCreate, IngredientUpdate
from app.app.utils.exceptions import ItemNotFoundError


class IngredientUseCases:
    ingredient_adapter = IngredientAdapter()
    adapter = BaseAdapter()

    def __init__(self, adapter: BaseAdapter) -> None:
        self.adapter = adapter

    def get_all(self) -> (List[Ingredient], int):
        return self.adapter.get_all()

    def get_by_id(self, id: str) -> Union[Ingredient, None]:
        return self.adapter.get_by_id(id)

    def create(self, new_item: dict) -> Ingredient:
        ingredient_to_create = IngredientCreate(**new_item)
        (response, ingredient_created) = self.adapter.create(ingredient_to_create.dict())
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return Ingredient(**ingredient_created, id=f"{ingredient_created['PK']}&{ingredient_created['SK']}")
        raise ItemNotFoundError("Error creating ingredient")

    def update(self, updated_item: dict) -> Ingredient:
        exist_ingredient = self.ingredient_adapter.exist(item_id=updated_item.get("_id", 0))

        if exist_ingredient:
            ingredient = IngredientUpdate(**updated_item)
            updated = self.adapter.update(ingredient.dict())
            return Ingredient(**updated)
        raise ItemNotFoundError("Error updating ingredient")

    def delete(self, _id: int):
        return self.adapter.delete(_id)

    def exist(self, _id: int):
        return self.adapter.exist(_id)
