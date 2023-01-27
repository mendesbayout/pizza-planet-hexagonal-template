from unittest.mock import patch

from api.app.adapters.dynamodb import dynamodb_adapter
from api.app.adapters.dynamodb.sizeAdapter import SizeAdapter
from api.app.models.size import Size


def test_size_get_by_id(size_created_response, valid_size_create_input):
    with patch.object(dynamodb_adapter, "get_by_id", return_value=size_created_response) as mock_get_by_id_method:
        result = SizeAdapter.get_by_id(item_id="SIZE#123")
        assert isinstance(result, Size)


def test_size_get_all(size_created_response, valid_size_create_input):
    with patch.object(dynamodb_adapter, "get_all", return_value=size_created_response) as mock_get_all_method:
        result, count = SizeAdapter.get_all()
        assert isinstance(result, list)