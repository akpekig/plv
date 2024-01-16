from jsf import JSF
from os.path import join
from plv.settings import ROOT_DIR
import json
import requests
import ast

# def test_nearest_stations(app, client):
#     # trips_by_origin_destination_req_body_schema = join(ROOT_DIR, "schemas", "trips_by_origin_destination_req_body.json")
#     # json_faker = JSF.from_json(trips_by_origin_destination_req_body_schema)
#     # fake_request = json_faker.generate()
#     req_body = {
#         "origin": "[7.43519,46.94567]",
#         "destination": "[7.63108, 46.76131]",
#     }

#     response = client.post("/nearest-stations", json=req_body)
#     result = json.loads(response.data.decode('utf-8'))

#     direct_response = requests.post(result["url"], json=result["body"], headers=result["headers"])
#     direct_response = direct_response.text

#     assert direct_response == result["body"]

#     assert response.status_code == 200
#     assert response.json == req_body

def test_nearest_stations(app, client):
    params = {
        "center": "[7.435077, 46.945616]"
    }

    response = client.get("/nearest-stations", query_string=params)

    assert response.data != None
    assert response.status_code == 200