from unittest.mock import patch
from api.app.adapters.dynamodb import IngredientAdapter, dynamodb_adapter
from api.app.models.ingredient import Ingredient, IngredientCreate


def test__ingredient_get_by_id_should_retrieve_ingredient_by_id(ingredient_created_response,
                                                                valid_ingredient_create_input):
    with patch.object(dynamodb_adapter, "create", return_value=ingredient_created_response) as mock_get_by_id_method:
        result = IngredientAdapter.create(valid_ingredient_create_input)
        assert isinstance(result, Ingredient)
        mock_get_by_id_method.assert_called()


def test_ingredient_get_all(ingredient_created_response, valid_ingredient_create_input):
    with patch.object(dynamodb_adapter, "get_all", return_value=ingredient_created_response) as mock_get_all_method:
        result, count = IngredientAdapter.get_all()
        assert isinstance(result, list)
        mock_get_all_method.assert_called()


def test_ingredient_create(valid_ingredient_create_input):
    with patch.object(dynamodb_adapter, "create") as mock_create_method:
        mock_create_method.assert_not_called()


def test_ingredient_get_by_id(ingredient_created_response, valid_ingredient_create_input):
    with patch.object(dynamodb_adapter, "get_by_id", return_value=ingredient_created_response) as mock_get_by_id_method:
        result = IngredientAdapter.get_by_id("ING#")
        assert isinstance(result, Ingredient)
