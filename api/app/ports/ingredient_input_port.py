from typing import List, Union

from app.app.adapters.base_adapter import BaseAdapter
from app.app.models.ingredient import Ingredient
from app.app.use_cases.ingredient_use_cases import IngredientUseCases


class IngredientInputPort:
    def __init__(self, adapter: BaseAdapter) -> None:
        self.ingredient_use_cases = IngredientUseCases(adapter)
        super().__init__()

    def get_all(self) -> (List[Ingredient], int):
        return self.ingredient_use_cases.get_all()

    def get_by_id(self, id: str) -> Union[Ingredient, None]:
        return self.ingredient_use_cases.get_by_id(id)

    def create(self, new_item: dict) -> Ingredient:
        return self.ingredient_use_cases.create(new_item)

    def update(self, updated_item: dict) -> Ingredient:
        return self.ingredient_use_cases.update(updated_item)

    def delete(self, _id: int):
        return self.ingredient_use_cases.delete(_id)
