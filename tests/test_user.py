import requests
import pytest
from assertpy.assertpy import assert_that
from json import dumps

from config import BASE_URI
from utils import user_helpers


def test_new_user_can_be_created(unique_user_data):
    unique_username = user_helpers.create_unique_user(unique_user_data)

    response = requests.get(f"{BASE_URI}/{unique_username}")
    assert_that(response.status_code).is_equal_to(200)

    # fluent assertions using assertpy
    response_user = response.json()
    assert_that(response_user).has_username(unique_username)
    assert_that(response_user).has_firstName("py_api_firstName")
    assert_that(response_user).has_lastName("py_api_lastName")


def test_new_user_can_be_updated(unique_user_data):
    unique_username = user_helpers.create_unique_user(unique_user_data)

    unique_user_status_code, unique_user_id = user_helpers.get_user_id_by_username(
        unique_username
    )
    assert_that(unique_user_status_code).is_equal_to(200)

    payload = dumps(
        {
            "id": unique_user_id,
            "username": unique_username,
            "firstName": "py_api_firstName_updated",
            "lastName": "py_api_lastName_updated",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0,
        }
    )

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.put(
        url=f"{BASE_URI}/{unique_username}", data=payload, headers=headers
    )
    assert_that(response.status_code).is_equal_to(200)

    response = requests.get(f"{BASE_URI}/{unique_username}")
    assert_that(response.status_code).is_equal_to(200)

    # fluent assertions using assertpy
    response_user = response.json()
    assert_that(response_user).has_username(unique_username)
    assert_that(response_user).has_firstName("py_api_firstName_updated")
    assert_that(response_user).has_lastName("py_api_lastName_updated")


def test_new_user_can_be_deleted(unique_user_data):
    unique_username = user_helpers.create_unique_user(unique_user_data)

    response = requests.delete(f"{BASE_URI}/{unique_username}")
    assert_that(response.status_code).is_equal_to(200)

    with pytest.raises(Exception) as e_info:
        user_helpers.get_user_id_by_username(unique_username)
    assert_that(str(e_info)).contains("ExceptionInfo KeyError('id')")
