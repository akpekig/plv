import json
import math
import networkx as nx


def json_load(fp):
    with open(fp) as f:
        return json.load(f)

parking = json_load("bike-car-parkings.json")
bikes = [park for park in parking if park["mietvelo_bezeichnung"] is not None]
cars = [] # TODO
train_lines = json_load("train-lines.json")

print(len(parking), len(bikes), len(train_lines))

# print(parking[0]["bezeichnung_offiziell"])
# print(train_lines[0]["bpk_anfang"])
# print(train_lines[0]["bpk_ende"])
# print(abs(train_lines[0]["km_ende"] - train_lines[0]["km_anfang"]))

def distance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance


def get_routes(origin_lat, origin_lon, destination_lat, destination_lon): # TODO car edges
    # walking speed : 4 km/h, cycling speed : 12 km/h, car speed : 60 km/h
    # if arrival/departure station has bike park, then we can go 5 km, otherwise 1 km by foot or 50 km by car if car park

    graph = nx.DiGraph()
    from script import get_train_journeys
    from extended_api import closest_stops

    direct_route = distance(origin_lat, origin_lon, destination_lat, destination_lon)
    graph.add_edge("origin", "destination", weight=direct_route / 60, transport="car")

    for start_stop in closest_stops(origin_lat, origin_lon, radius=10):
        start_position = start_stop["centroid"]["coordinates"]
        start_distance = distance(start_position[1], start_position[0], origin_lat, origin_lon)
        if start_distance < 1:
            graph.add_edge("origin", start_stop["name"], weight=start_distance / 4, transport="walk")
        start_bike_park = [park for park in bikes if park["bezeichnung_offiziell"] == start_stop["name"]]
        if len(start_bike_park) > 0 and start_distance < 5:
            graph.add_edge("origin", start_stop["name"], weight=start_distance / 12, transport="bike")

        for end_stop in closest_stops(destination_lat, destination_lon, radius=10):
            end_position = end_stop["centroid"]["coordinates"]
            end_distance = distance(end_position[1], end_position[0], destination_lat, destination_lon)
            end_bike_park = [park for park in bikes if park["bezeichnung_offiziell"] == end_stop["name"]]
            if end_distance < 1:
                graph.add_edge(end_stop["name"], "destination", weight=end_distance / 4, transport="walk")
            if len(end_bike_park) > 0 and end_distance < 5:
                graph.add_edge(end_stop["name"], "destination", weight=end_distance / 12, transport="bike")

            for journey in get_train_journeys(start_stop["id"], end_stop["id"]):
                try:
                    duration_minutes = int(journey["duration"][-3:-1])
                except:
                    duration_minutes = int(journey["duration"][-2:-1])
                try:
                    duration_hours = int(journey["duration"][-5:-4]) if len(journey["duration"]) > 5 else 0
                except:
                    duration_hours = int(journey["duration"][-4:-3])
                duration = duration_hours + duration_minutes / 60
                graph.add_edge(start_stop["name"], end_stop["name"], weight=duration, transport="train")

    # print(graph.edges.data())
    shortest_path = nx.astar_path(graph, "origin", "destination")
    duration = sum(graph.get_edge_data(u, v)["weight"] for u, v in zip(shortest_path, shortest_path[1:]))
    modes = [graph.get_edge_data(u, v)["transport"] for u, v in zip(shortest_path, shortest_path[1:])]
    return shortest_path, modes, duration


if __name__ == "__main__":
    # Bern to Zurich
    print(get_routes(46.948832290498416, 7.43913088992393, 47.378176674223226, 8.540212349099065))

    # Lausanne to Zurich
    print(get_routes(46.51679183546494, 6.629092303198574, 47.378176674223226, 8.540212349099065))

    # Zurich to Lausanne
    # print(get_routes(47.378176674223226, 8.540212349099065, 46.51679183546494, 6.629092303198574))
