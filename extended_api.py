import requests
from flask import Flask
from helpers import get_token
from markupsafe import escape
from settings import JOURNEY_SERVICE_BASE_URL

app = Flask(__name__)

@app.route("/api/closest-stops/<lat>/<lon>/<radius>")
def closest_stops(lat: float, lon: float, radius: int):
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
        "radius": escape(radius),
    }
    query = requests.get(url, headers=headers, params=params).json()
    stops = query["places"]
    return stops
