from os.path import dirname, join

import jsonschema
import json
import requests
from flask import Flask, request
from jsonschema_typed import JSONSchema
from markupsafe import escape

from api.helpers import get_token, validate_req_body
from plv.settings import JOURNEY_SERVICE_BASE_URL, ROOT_DIR, MILE_TO_METER

def create_app():
    app = Flask(__name__)

    @app.route("/nearest-stations")
    def nearest_stations():
        """
        Retrieves stations in a 1 mile radius based on the request body.

        Returns:
            list: A list of stations.
        """
        token = get_token()
        url = f"{JOURNEY_SERVICE_BASE_URL}/v3/places/by-coordinates-geojson"
        headers = {
            "Authorization": f"Bearer {token}",
            "accept": "application/json",
            "Accept-Language": "en",
            "Content-Type": "application/json"
        }
        params = request.args.to_dict()
        params["radius"] = MILE_TO_METER
        query = requests.get(url, headers=headers, params=params).json()
        stations = query["places"]
        return stations

    return app