from api.app.models.order_detail import OrderDetail


def test_create_order_detail(order_detail_adapter):
    order_detail_data = {
        "product_id": "1",
        "product_name": "Test Product",
        "quantity": 1,
        "price": 9.99
    }
    order_detail = order_detail_adapter.create(order_detail_data)
    assert order_detail.product_id == "1"
    assert order_detail.product_name == "Test Product"
    assert order_detail.quantity == 1
    assert order_detail.price == 9.99


def test_get_by_id_order_detail(order_detail_adapter):
    order_detail_data = {
        "product_id": "1",
        "product_name": "Test Product",
        "quantity": 1,
        "price": 9.99
    }
    created_order_detail = order_detail_adapter.create(order_detail_data)
    order_detail_id = created_order_detail.id
    retrieved_order_detail = order_detail_adapter.get_by_id(order_detail_id)
    assert retrieved_order_detail.product_id == "1"
    assert retrieved_order_detail.product_name == "Test Product"
    assert retrieved_order_detail.quantity == 1
    assert retrieved_order_detail.price == 9.99


def test_get_all_order_detail(order_detail_adapter):
    order_detail_data = {
        "product_id": "1",
        "product_name": "Test Product",
        "quantity": 1,
        "price": 9.99
    }
    order_detail_adapter.create(order_detail_data)
    order_detail_list, count = order_detail_adapter.get_all()
    assert count >= 1
    assert isinstance(order_detail_list, list)
    assert all(isinstance(order_detail, OrderDetail) for order_detail in order_detail_list)


def test_update_order_detail(order_detail_adapter):
    order_detail_data = {
        "product_id": "1",
        "product_name": "Test Product",
        "quantity": 1,
        "price": 9.99
    }
    created_order_detail = order_detail_adapter.create(order_detail_data)
    created_order_detail.quantity = 2
    updated_order_detail = order_detail_adapter.update(created_order_detail.__dict__)
    assert updated_order_detail.quantity == 2

