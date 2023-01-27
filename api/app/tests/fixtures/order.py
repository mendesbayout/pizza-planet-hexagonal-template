from unittest.mock import patch

import pytest

from utils.functions import (shuffle_list, get_random_sequence,
                             get_random_string)

from api.app.adapters.dynamodb import dynamodb_adapter
from api.app.adapters.dynamodb.orderAdapter import OrderAdapter


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_uri():
    return '/order'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    size_id = create_size.get('_id')
    return {
        **client_data_mock(),
        'ingredients': ingredients,
        'size_id': size_id
    }


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'size_id': shuffle_list(sizes)[0]
        })
        orders.append(new_order)
    return orders


@pytest.fixture
def order_created_response():
    return {
        "PK": "ORD#123",
        "SK": "ORD#123",
        "customer_name": "John Doe",
        "total_price": 12.99
    }


@pytest.fixture
def valid_order_create_input():
    return {
        "customer_name": "John Doe",
        "total_price": 12.99
    }


def test_order_create(valid_order_create_input):
    with patch.object(dynamodb_adapter, "create") as mock_create_method:
        OrderAdapter.create(valid_order_create_input)
        mock_create_method.assert_called_with({
            "PK": "ORD#",
            "SK": "ORD#",
            "customer_name": valid_order_create_input["customer_name"],
            "total_price": valid_order_create_input["total_price"]
        })
