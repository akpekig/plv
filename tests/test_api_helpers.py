from unittest.mock import patch

import requests

from api.helpers import get_token, validate_req_body


@patch("api.helpers.requests.post")
def test_get_token(mock_post):
    mock_post.return_value.json.return_value = {"access_token": "1234"}
    assert get_token() == "1234"


def test_validate_req_body_valid():
    req_body = {"name": "John", "age": 25}
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
    }
    assert validate_req_body(req_body, schema) == True


def test_validate_req_body_invalid():
    req_body = {"name": "John", "age": "25"}
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
    }
    assert validate_req_body(req_body, schema) == False
