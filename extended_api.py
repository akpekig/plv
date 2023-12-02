import requests
import jsonschema
from jsonschema_typed import JSONSchema
from flask import Flask, Request
from helpers import get_token, validate_req_body
from markupsafe import escape
from settings import JOURNEY_SERVICE_BASE_URL
from os.path import join, dirname

app = Flask(__name__)

TRIPS_BY_ORIGIN_DESTINATION_REQ_BODY_SCHEMA = join(dirname(__file__), 'schemas/maps_trips_by_origin_destination_req_body.json')


@app.route("/api/trips/get", methods=['POST'])
def get_trips():
    """
    Retrieves the trips based on the request body.

    Returns:
        list: A list of trips.
    """
    token = get_token()
    req_body: JSONSchema[TRIPS_BY_ORIGIN_DESTINATION_REQ_BODY_SCHEMA] = Request.get_json()
    if not validate_req_body(req_body, TRIPS_BY_ORIGIN_DESTINATION_REQ_BODY_SCHEMA):
        return "Invalid request body.", 400
    req_body["originRadius"] = 1000
    req_body["destinationRadius"] = 500

    url = f"{JOURNEY_SERVICE_BASE_URL}/v3/trips/by-origin-destination"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    query = requests.post(url, headers=headers, data=req_body).json()
    stops = query["trips"]
    return stops