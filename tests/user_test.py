import requests
from assertpy.assertpy import assert_that
from config import BASE_URI

def test_read_users_has_bob():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(200)