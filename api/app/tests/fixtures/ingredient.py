import datetime
import pytest


@pytest.fixture
def ingredient_created_response():
    ingredient_created = {
        'PK': 'ING#000',
        'SK': 'ING#000',
        'name': 'flour',
        'price': 0.5,
        'creation_date': datetime.datetime.now().timestamp(),
        'updated_date': datetime.datetime.now().timestamp()
    }
    response = {'ResponseMetadata': {'HTTPStatusCode': 200}}
    return response, ingredient_created


@pytest.fixture
def valid_ingredient_create_input():
    valid_input = {
        'name': 'flour',
        'price': 0.5
    }
    return valid_input
