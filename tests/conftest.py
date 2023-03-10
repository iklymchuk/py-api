import pytest
from utils import file_reader
from uuid import uuid4


@pytest.fixture
def unique_user_data():
    payload = file_reader.read_file("create_user.json")
    unique_username = f"User {str(uuid4())}"
    payload["username"] = unique_username
    yield payload

@pytest.fixture
def updated_user_data():
    payload = file_reader.read_file("update_user.json")
    yield payload


@pytest.fixture
def user_schema():
    payload = file_reader.read_file("user_schema.json")
    yield payload
