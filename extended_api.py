import requests
from flask import Flask
from helpers import get_token
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
    return stops

@app.route("/api/best-entrance/<stop_id>")
def best_entrance(stop_id: str):
    """
    Retrieves the best entrance for the given stop.

    Args:
        stop_id (str): The ID of the stop.

    Returns:
        dict: The best entrance for the given stop.
    """
    url = f"{JOURNEY_SERVICE_BASE_URL}/v3/stops/{stop_id}/best-entrance"
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    query = requests.get(url, headers=headers).json()
    entrance = query["bestEntrance"]
    return entrance