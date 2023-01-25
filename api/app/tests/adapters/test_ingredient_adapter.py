from unittest.mock import patch

import pytest
from pydantic import ValidationError

from app.app.adapters.dynamodb import IngredientAdapter, dynamodb_adapter
from app.app.models.ingredient import Ingredient, IngredientCreate


def test__ingredient_get_by_id_should_retrieve_ingredient_by_id(ingredient_created_response, valid_ingredient_create_input):
    with patch.object(dynamodb_adapter, "create", return_value=ingredient_created_response) as mock_get_by_id_method:
        result = IngredientAdapter.create(valid_ingredient_create_input)
        assert isinstance(result, Ingredient)
        # assert result.name == valid_ingredient["name"]
        # assert result.price == valid_ingredient["price"]


