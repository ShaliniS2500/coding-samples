import osmnx as ox
import networkx as nx
import numpy as np

place = "Montville, New Jersey, USA"
G = ox.graph_from_place(place, network_type="drive")
G = ox.routing.add_edge_speeds(G)
G = ox.routing.add_edge_travel_times(G)

np.random.seed(42)
for u, v, k, data in G.edges(keys=True, data=True):
    highway_type = data.get("highway", "residential")
    if isinstance(highway_type, list):
        highway_type = highway_type[0]

    if highway_type in ["motorway", "trunk", "primary"]:
        congestion_factor = np.random.uniform(1.5, 2.5)
    elif highway_type in ["secondary", "tertiary"]:
        congestion_factor = np.random.uniform(1.2, 1.8)
    else:
        congestion_factor = np.random.uniform(1.0, 1.3)

    free_flow_time = data.get("travel_time", 1.0)
    data["traffic_travel_time"] = free_flow_time * congestion_factor

location_a = (40.91358, -74.35103)
location_b = (40.89692, -74.37518)

node_a = ox.nearest_nodes(G, X=location_a[1], Y=location_a[0])
node_b = ox.nearest_nodes(G, X=location_b[1], Y=location_b[0])

route = ox.routing.shortest_path(G, node_a, node_b, weight="traffic_travel_time")
total_travel_time_seconds = nx.shortest_path_length(G, node_a, node_b, weight="traffic_travel_time")
travel_time_minutes = total_travel_time_seconds / 60

print(f"Total travel time: {total_travel_time_seconds:.1f} seconds ({travel_time_minutes:.2f} minutes)")
ox.plot_graph_route(G, route, route_color="g")


