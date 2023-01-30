import requests
from json import dumps
from assertpy.assertpy import assert_that

from config import BASE_URI


def create_unique_user(body):
    payload = dumps(body)

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

    return body["username"]


def get_user_id_by_username(username):
    response = requests.get(f"{BASE_URI}/{username}")
    return response.status_code, response.json()["id"]
