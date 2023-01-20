import requests
from assertpy.assertpy import assert_that
from json import dumps
from uuid import uuid4

from config import BASE_URI

def create_new_user():
    unique_username = f"User {str(uuid4())}"
    payload = dumps({
        "username": unique_username,
        "firstName": "py_api_firstName",
        "lastName": "py_api_lastName",
        "userStatus": 0
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=BASE_URI, data=payload, headers=headers)

    assert_that(response.status_code).is_equal_to(200)
    return unique_username