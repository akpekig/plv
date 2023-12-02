from settings import MICROSOFT_TOKEN_URL, MICROSOFT_TOKEN_GRANT_TYPE, MICROSOFT_TOKEN_SCOPE, MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET
import requests

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
        "client_secret": MICROSOFT_CLIENT_SECRET
    }
    query = requests.post(url, data=params).json()
    token = query["access_token"]
    return token

def get_closest_stops(lat, lon):
    """
    Retrieves the closest stops based on the given latitude and longitude.

    Args:
        lat (float): The latitude coordinate.
        lon (float): The longitude coordinate.

    Returns:
        list: A list of closest stops.
    """
    pass