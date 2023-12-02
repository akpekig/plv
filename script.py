import requests


def get_token():
    url = "https://login.microsoftonline.com/2cda5d11-f0ac-46b3-967d-af1b2e1bd01a/oauth2/v2.0/token"
    params = {
        "grant_type": "client_credentials",
        "scope": "c11fa6b1-edab-4554-a43d-8ab71b016325/.default",
        "client_id": "f132a280-1571-4137-86d7-201641098ce8",
        "client_secret": "MU48Q~IuD6Iawz3QfvkmMiKHtfXBf-ffKoKTJdt5"
    }
    return requests.post(url, data=params).json()

def get_train_journeys(origin_station, destination_station):
    url = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"
    token = get_token()["access_token"]
    headers = {
        "Authorization": "Bearer {}".format(token),
        "accept": "application/json",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    params = {
        "origin": origin_station,
        "destination": destination_station,
        "date": "2023-04-18",
        "time": "13:07",
        "mobilityFilter": {
            "walkSpeed": 50,
        },
        "includeAccessibility": "ALL"
    }
    return requests.post(url, headers=headers, json=params).json()["trips"]


if __name__ == "__main__":
    # OPUIC station ids
    trips = get_train_journeys("8503000", "8507000") # each trip contains keys "duration", "transfers", "legs"
    for i, trip in enumerate(trips, 1):
        print("trip {} from {} to {} is {}, with {} transfers".format(i, "8503000", "8507000", trip["duration"][2:], trip["transfers"]))
    print({**trips[0], "id": 0, "legs": 0})
