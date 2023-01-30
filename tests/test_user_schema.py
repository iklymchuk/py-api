import json

import requests
from assertpy.assertpy import assert_that
from cerberus import Validator

from config import BASE_URI
from utils import user_helpers

schema = {
    "id": {"type": "integer"},
    "username": {"type": "string"},
    "firstName": {"type": "string"},
    "lastName": {"type": "string"},
    "email": {"type": "string"},
    "password": {"type": "string"},
    "phone": {"type": "string"},
    "userStatus": {"type": "integer"},
}


def test_get_user_operation_has_expected_schema(unique_user_data):
    unique_username = user_helpers.create_unique_user(unique_user_data)

    response = requests.get(f"{BASE_URI}/{unique_username}")
    assert_that(response.status_code).is_equal_to(200)

    user = json.loads(response.text)
    validator = Validator(schema)

    assert_that(validator.validate(user), description=validator.errors).is_true()
