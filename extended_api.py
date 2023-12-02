import requests
from flask import Flask
from helpers import get_token, get_closest_stops
from markupsafe import escape
from settings import JOURNEY_SERVICE_BASE_URL

app = Flask(__name__)

@app.route("/api/closest-stops/<lat>/<lon>")
def closest_stops(lat: float, lon: float):
    """
    Retrieves the closest stops based on the given latitude and longitude.

    Args:
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.

    Returns:
        list: A list of closest stops.
    """
    url = f"{JOURNEY_SERVICE_BASE_URL}/v3/places/by-coordinates"
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    params = {
        "longitude": escape(lon),
        "latitude": escape(lat),
        "radius": "1609",
    }
    query = requests.get(url, headers=headers, params=params).json()
    stops = query["places"]
    stops = get_closest_stops(stops)
    return stops