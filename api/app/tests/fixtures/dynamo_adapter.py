from unittest import mock
import pytest
from boto3.dynamodb.table import Table
from api.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter


@pytest.fixture
def dynamo():
    return DynamoDBAdapter("PK", "SK")


@pytest.fixture
def get_all(dynamo):
    return dynamo.get_all()


@pytest.fixture
def get_by_field(dynamo):
    return lambda field, value: dynamo.get_by_field(field, value)


@pytest.fixture
def get_by_id(dynamo):
    return lambda item_id: dynamo.get_by_id(item_id)


@pytest.fixture
def get_by_partition_key(dynamo):
    return lambda partition_key: dynamo.get_by_partition_key(partition_key)


@pytest.fixture
def create(dynamo):
    return lambda new_item: dynamo.create(new_item)


@pytest.fixture
def delete(dynamo):
    return lambda item_id: dynamo.delete(item_id)


@pytest.fixture
def update():
    updated_item = {"id": 1, "field1": "new_value1", "field2": "new_value2"}
    return updated_item


@pytest.fixture
def dynamodb_table():
    with mock.patch('boto3.resource') as mock_boto3_resource:
        mock_table = mock.create_autospec(Table)
        mock_boto3_resource().Table.return_value = mock_table
        yield mock_table
