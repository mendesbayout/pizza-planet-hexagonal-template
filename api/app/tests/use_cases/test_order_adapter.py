from unittest.mock import patch

from api.app.adapters.dynamodb import dynamodb_adapter
from api.app.adapters.dynamodb.orderAdapter import OrderAdapter
from api.app.models.order import Order


def test_order_get_by_id(order_created_response, valid_order_create_input):
    with patch.object(dynamodb_adapter, "get_by_id", return_value=order_created_response) as mock_get_by_id_method:
        result = OrderAdapter.get_by_id("ORD#123")
        assert isinstance(result, Order)


def test_order_get_all(order_created_response, valid_order_create_input):
    with patch.object(dynamodb_adapter, "get_all", return_value=order_created_response) as mock_get_all_method:
        result, count = OrderAdapter.get_all()
        assert isinstance(result, list)
