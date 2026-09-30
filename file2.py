import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

G = nx.Graph()
countries = ["Thailand", "Malaysia", "Singapore", "Indonesia", "Vietnam"]
G.add_nodes_from(countries)

# Add edges representing transportation routes
G.add_edges_from(
    [
        ("Thailand", "Malaysia"),
        ("Malaysia", "Singapore"),
        ("Malaysia", "Indonesia"),
        ("Indonesia", "Singapore"),
        ("Indonesia", "Vietnam"),
        ("Vietnam", "Singapore"),
    ]
)

# Set edge weights to represent factors like distance or travel time
edge_weights = {
    ("Thailand", "Malaysia"): 500,  # Distance in kilometers
    ("Malaysia", "Singapore"): 50,
    ("Malaysia", "Indonesia"): 200,
    ("Indonesia", "Singapore"): 100,
    ("Indonesia", "Vietnam"): 300,
    ("Vietnam", "Singapore"): 150,
}

nx.set_edge_attributes(G, edge_weights, "weight")


# Plot the graph
pos = nx.spring_layout(G)  # Positions of the nodes
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=800,
    font_size=10,
    font_weight="bold",
)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.5, alpha=0.7)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_weights, font_color="red", font_size=8
)
plt.title("Hello South-East Asia! Analyzing transportation Networks")

plt.show()