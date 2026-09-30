import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Country": [
        "Australia",
        "New Zealand",
        "Fiji",
        "Solomon Islands",
        "Samoa",
        "Tonga",
    ],
    "Capital": ["Canberra", "Wellington", "Suva", "Honiara", "Apia", "Nuku'alofa"],
    "Latitude": [-35.282, -41.286, -18.166, -9.749, -13.831, -21.139],
    "Longitude": [149.128, 174.776, 178.441, 160.189, -171.769, -175.204],
    "Next_country": ["New Zealand", "Fiji", "Solomon Islands", "Samoa", "Tonga", ""],
}

df_oceania = pd.DataFrame(data)
print(df_oceania)

# Exclude rows with empty 'Next_country' values
df_oceania = df_oceania[df_oceania["Next_country"] != ""]

G = nx.from_pandas_edgelist(
    df_oceania, source="Country", target="Next_country", create_using=nx.DiGraph()
)

# Set the latitude and longitude as node positions
pos = {
    country: (longitude, latitude)
    for country, latitude, longitude in zip(
        df_oceania["Country"], df_oceania["Latitude"], df_oceania["Longitude"]

    )
}

# Assign a default position for nodes without specified latitude and longitude
default_pos = (0, 0)  # You can change the default position here
pos = {node: pos.get(node, default_pos) for node in G.nodes}

nx.set_node_attributes(G, pos, "pos")
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    arrows=True,
    node_color="lightblue",
    node_size=100,
    font_size=10,
)
plt.title("Hello Oceania: Planning trips with other python libraries")

sns.set_style("whitegrid")

fig, ax = plt.subplots(figsize=(8,6))

ax.set_title("Network Graph", fontsize=16)

ax.set_xlabel("Longitude", fontsize=12)
ax.set_ylabel("Latitude", fontsize=12)

node_labels = nx.get_node_attributes(G, "label")
nx.draw_networkx_labels(G, pos=pos, labels=node_labels, font_size=10)

nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_color="lightblue",
    node_size=500,
    edge_color="gray",
    width=1.5,
    arrows=True,
    ax=ax,
)

# Customize the grid
ax.grid(True, which="both", linestyle="--")

# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Ensure axes are displayed
ax.axis("on")

# Add seaborn styling elements
sns.despine(
    ax=ax, left=True, bottom=False
)  # See how the left ax line is removed, but not the bottom one


# Add a title and display the plot
plt.title("Hello Oceania 2: Plotting with Seaborn")

import scipy

adj_matrix_scipy = nx.to_scipy_sparse_array(G)
clustering_coefficient = nx.average_clustering(G)

components = scipy.sparse.csgraph.connected_components(adj_matrix_scipy, directed=True)

print("Adjacency Matrix:")
print(adj_matrix_scipy.toarray())
print("Clustering Coefficient:", clustering_coefficient)
print("Connected Components:", components)

G.add_node("Vanuatu")
G.add_node("Marshall Islands")
G.add_edge("Vanuatu", "Marshall Islands")

adj_matrix_scipy = nx.to_scipy_sparse_array(G)
components = scipy.sparse.csgraph.connected_components(adj_matrix_scipy)

print("Adjacency Matrix:")
print(adj_matrix_scipy.toarray())
print("Clustering Coefficient:", clustering_coefficient)
print("Connected Components:", components)

plt.show()