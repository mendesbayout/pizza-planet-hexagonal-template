from api.app.adapters.dynamodb.dynamodb_adapter import DynamoDBAdapter


def test_get_all(get_all):
    result = get_all()
    assert "Items" in result


def test_get_by_field(get_by_field):
    result = get_by_field("field", "value")
    assert "Items" in result


def test_get_by_id(get_by_id):
    result = get_by_id("item_id")
    assert "Item" in result


def test_get_by_partition_key(get_by_partition_key):
    result = get_by_partition_key("partition_key")
    assert "Items" in result


def test_create(create):
    result, new_item = create({"PK": "pk", "SK": "sk"})
    assert result["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert new_item == {"PK": "pk", "SK": "sk"}


def test_delete(dynamodb_table):
    result = dynamodb_table.delete(Key={'PK': 'pk', 'SK': 'sk'})
    assert result["ResponseMetadata"]["HTTPStatusCode"] == 200


def test_update(dynamodb_table):
    dynamodb_table.put_item(Item={'PK': 'pk', 'SK': 'sk', 'value': 'original_value'})
    result = dynamodb_table.update_item(
        Key={'PK': 'pk', 'SK': 'sk'},
        UpdateExpression='SET value = :val',
        ExpressionAttributeValues={':val': 'updated_value'}
    )
    assert result["ResponseMetadata"]["HTTPStatusCode"] == 200
    item = dynamodb_table.get_item(Key={'PK': 'pk', 'SK': 'sk'})['Item']
    assert item['value'] == 'updated_value'
