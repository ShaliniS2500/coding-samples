import matplotlib.pyplot as plt
import networkx as nx

# G = nx.Graph()
#
# # Add nodes (countries)
# african_countries = ["Gabon", "Kenya", "Tanzania", "South Africa", "Equatorial Guinea"]
# G.add_nodes_from(african_countries)
#
# # Add edges (neighboring countries)
# G.add_edges_from(
#     [
#         ("Gabon", "Kenya"),
#         ("Gabon", "Tanzania"),
#         ("Gabon", "South Africa"),
#         ("Gabon", "Equatorial Guinea"),
#         ("Kenya", "Gabon"),
#         ("Kenya", "Tanzania"),
#         ("Kenya", "South Africa"),
#         ("Kenya", "Equatorial Guinea"),
#         ("Tanzania", "Gabon"),
#         ("Tanzania", "Kenya"),
#         ("Tanzania", "South Africa"),
#         ("Tanzania", "Equatorial Guinea"),
#         ("South Africa", "Gabon"),
#         ("South Africa", "Kenya"),
#         ("South Africa", "Tanzania"),
#         ("South Africa", "Equatorial Guinea"),
#         ("Equatorial Guinea", "Gabon"),
#         ("Equatorial Guinea", "Kenya"),
#         ("Equatorial Guinea", "Tanzania"),
#         ("Equatorial Guinea", "South Africa"),
#     ]
# )
#
# G.nodes["Gabon"]["National Parks"] = 13
# G.nodes["Kenya"]["National Parks"] = 25
# G.nodes["Tanzania"]["National Parks"] = 22
# G.nodes["South Africa"]["National Parks"] = 23
# G.nodes["Equatorial Guinea"]["National Parks"] = 3
#
# # Add visa requirements
# nodes = ["Gabon", "Kenya", "Tanzania", "South Africa", "Equatorial Guinea"]
# labels = ["E-VISA", "E-VISA", "E-VISA", "NO-VISA", "VISA"]
#
# # Add labels to nodes using a loop
# for node, label in zip(nodes, labels):
#     G.nodes[node]["visa_type"] = label
#
# G.edges[("Gabon", "Kenya")]["distance"] = 4778  # Libreville - Nairobi
# G.edges[("Gabon", "Tanzania")]["distance"] = 5038  # Libreville - Dodoma
# G.edges[("Gabon", "South Africa")][
#     "distance"
# ] = 5042  # Libreville - Pretoria --> I chose this one capital
# G.edges[("Gabon", "Equatorial Guinea")]["distance"] = 620  # Libreville - Bata
# G.edges[("Kenya", "Tanzania")]["distance"] = 678
# G.edges[("Kenya", "South Africa")]["distance"] = 3745
# G.edges[("Kenya", "Equatorial Guinea")]["distance"] = 4740
# G.edges[("Tanzania", "South Africa")]["distance"] = 3070
# G.edges[("Tanzania", "Equatorial Guinea")]["distance"] = 5275
# G.edges[("South Africa", "Equatorial Guinea")]["distance"] = 5441
#
# # Get the node attributes
# visa_types = nx.get_node_attributes(G, "visa_type")
# national_parks = nx.get_node_attributes(G, "National Parks")
#
# # And get the edges attributes
# edge_distances = nx.get_edge_attributes(G, "distance")
#
# # Define latitude and longitude coordinates of the capital cities
# coordinates = {
#     "Gabon": (9.45, 0.3833),  # Libreville
#     "Kenya": (36.8172, -1.2864),  # Nairobi
#     "Tanzania": (39.2083, -6.7924),  # Dodoma
#     "South Africa": (28.1881, -25.7461),  # Pretoria
#     "Equatorial Guinea": (8.7737, 3.7523),  # Malabo
# }
#
# # Define colors based on visa types
# color_mapping = {"E-VISA": "lightblue", "NO-VISA": "lightgreen", "VISA": "lightcoral"}
# node_colors = [color_mapping[visa_types[node]] for node in G.nodes]
#
# node_sizes = [national_parks[node] * 20 for node in G.nodes]
#
# coord = {node: coordinates[node] for node in G.nodes}
#
# nx.draw(
#     G,
#     pos=coord,
#     with_labels=True,
#     node_color=node_colors,
#     node_size=node_sizes,
#     font_size=7,
#     edge_color="#666",
#     width=0.8,
# )
#
# nx.draw_networkx_edge_labels(
#     G,
#     coordinates,
#     edge_labels=edge_distances,
#     font_size=7,
#     bbox=dict(facecolor="white", edgecolor="none", alpha=0.8),
#     verticalalignment="center",
#     label_pos=0.45,
# )
#
# # Create the legend with color boxes and labels
# legend_elements = [
#     plt.Line2D(
#         [0],
#         [0],
#         marker="o",
#         color="w",
#         markerfacecolor=color_mapping[label],
#         markersize=8,
#     )
#     for label in color_mapping.keys()
# ]
# legend_labels = list(color_mapping.keys())
#
# # Add the legend to the plot
# plt.legend(legend_elements, legend_labels, loc="lower right", fontsize="small")
#
#
# # Add a title to the graph
# plt.title(
#     "Hello Africa: Natural parks, visa requirements and distance between countries"
# )
#
# plt.show()
#

# G = nx.Graph()
#
# # Add nodes and edges for Central Asian countries
# G.add_nodes_from(
#     ["Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"]
# )
# G.add_edges_from(
#     [
#         ("Kazakhstan", "Kyrgyzstan"),
#         ("Kyrgyzstan", "Tajikistan"),
#         ("Tajikistan", "Turkmenistan"),
#         ("Turkmenistan", "Uzbekistan"),
#         ("Uzbekistan", "Kazakhstan"),
#     ]
# )
#
# # latitude and longitude coordinates of the capital cities in Central Asia
# coordinates = {
#     "Kazakhstan": (71.4491, 51.1694),  # Nur-Sultan (formerly known as Astana)
#     "Kyrgyzstan": (74.5698, 42.8746),  # Bishkek
#     "Tajikistan": (68.7738, 38.5737),  # Dushanbe
#     "Turkmenistan": (58.3261, 37.9601),  # Ashgabat
#     "Uzbekistan": (69.2401, 41.2995),  # Tashkent
# }
#
# # Draw the graph with node positions
# pos = nx.spring_layout(G, pos=coordinates, fixed=coordinates.keys())
#
# # Draw nodes and edges
# nx.draw_networkx(
#     G, pos=pos, with_labels=True, node_color="pink", node_size=200, font_size=8
# )
# nx.draw_networkx_edges(G, pos=pos, edge_color="gray")
#
# # Add a title to the graph
# plt.title("Hello Central Asia: Finding the shortest Path")
#
# plt.show()
#
# print(nx.shortest_path(G, "Kazakhstan", "Turkmenistan"))
# print(nx.single_source_dijkstra_path(G, "Kazakhstan"))
#
# # with breadth-first
# bfs_traversal = list(nx.dfs_tree(G, "Turkmenistan"))
#
# print("BFS traversal:", bfs_traversal)

G = nx.Graph()

"""

"""
countries = [
    "Argentina",
    "Bolivia",
    "Brazil",
    "Chile",
    "Colombia",
    "Ecuador",
    "Guyana",
    "Paraguay",
    "Peru",
    "Suriname",
    "Uruguay",
    "Venezuela",
]
G.add_nodes_from(countries)


flight_connections = [
    ("Argentina", "Brazil"),
    ("Argentina", "Chile"),
    ("Argentina", "Bolivia"),
    ("Brazil", "Colombia"),
    ("Brazil", "Ecuador"),
    ("Colombia", "Ecuador"),
    ("Colombia", "Venezuela"),
    ("Ecuador", "Peru"),
    ("Guyana", "Suriname"),
    ("Paraguay", "Brazil"),
    ("Peru", "Chile"),
    ("Suriname", "Guyana"),
    ("Uruguay", "Argentina"),
]


G.add_edges_from(flight_connections)
louvain = nx.community.louvain_communities(G)

for index, community in enumerate(louvain, 1):
    print(f"community {index} : {community}")


    community_dict = {}
    for i, community in enumerate(louvain):
        for country in community:
            community_dict[country] = i


    # node_colors = [community_dict.get(country) for country in G.nodes]
    #
    # pos = nx.spring_layout(G)
    #
    # plt.figure(figsize=(5, 5))
    #
    # nx.draw(
    #     G,
    #     pos=pos,
    #     node_color=node_colors,
    #     with_labels=True,
    #     node_size=100,
    #     cmap=plt.cm.Set1,
    # )
    plt.title("Hello South America! Seeking connections with the Louvain Algorithm")



    G.degree()
    degree_sequence = [degree for node, degree in G.degree()]
    degree_count = nx.degree_histogram(G)
    plt.bar(range(len(degree_count)), degree_count, width=0.8, color="lightblue")
    plt.xlabel("Degree")
    plt.ylabel("Number of nodes")
    plt.title("Degree Distribution for South American country nodes")


    clustering_coefficients = nx.clustering(G)

    # Print the clustering coefficient of each node
    for node, cc in clustering_coefficients.items():
        print(f"Clustering coefficient of Node {node}: {cc}")

    avg_clustering_coefficient = nx.average_clustering(G)
    print(f"Average clustering coefficient: {avg_clustering_coefficient}")

    plt.show()

