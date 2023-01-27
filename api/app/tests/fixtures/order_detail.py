import pytest

from api.app.adapters.dynamodb.order_detail_adapter import OrderDetailAdapter


@pytest.fixture()
def order_detail_adapter():
    return OrderDetailAdapter()