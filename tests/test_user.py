import requests
from assertpy.assertpy import assert_that

from config import BASE_URI
from utils import user_helpers

def test_new_user_can_be_created():
    unique_username = user_helpers.create_new_user()

    response = requests.get(f"{BASE_URI}/{unique_username}")
    assert_that(response.status_code).is_equal_to(200)
    #print(response.json()['username'])
    assert_that(response.json()['username']).contains(f"{unique_username}")

