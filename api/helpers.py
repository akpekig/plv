import json

import jsonschema
import requests

from plv.settings import (
    MICROSOFT_CLIENT_ID,
    MICROSOFT_CLIENT_SECRET,
    MICROSOFT_TOKEN_GRANT_TYPE,
    MICROSOFT_TOKEN_SCOPE,
    MICROSOFT_TOKEN_URL,
)


def get_token():
    """
    Retrieves an access token from Microsoft using the specified parameters.

    Returns:
        str: The access token.

    Raises:
        KeyError: If the access token is not found in the response.
    """
    url = MICROSOFT_TOKEN_URL
    params = {
        "grant_type": MICROSOFT_TOKEN_GRANT_TYPE,
        "scope": MICROSOFT_TOKEN_SCOPE,
        "client_id": MICROSOFT_CLIENT_ID,
        "client_secret": MICROSOFT_CLIENT_SECRET,
    }
    query = requests.post(url, data=params).json()
    token = query["access_token"]
    return token


def validate_req_body(req_body: dict, schema: dict):
    """
    Validates request body against schema.

    Args:
        req_body (dict): The request body.

    Raises:
        jsonschema.exceptions.ValidationError: If the request body is invalid.
    """
    try:
        jsonschema.validate(req_body, schema)
        return True
    except jsonschema.ValidationError:
        return False
