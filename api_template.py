import requests
def get_station_name(station_dict):
    station_name = station_dict.get('designationOfficial', 'N/A')
    return station_name

def get_station_name_api():
    query = requests.get("https://servicepoints.api.sbb.ch/v1/CH/STOP/ids=BNWD", headers={

    })
    print(query)
    station_name = get_station_name(query.json())
    return station_name

print(get_station_name_api())
