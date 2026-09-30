import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node("A")
G.add_nodes_from([2, 3, 4])
G.add_node(5, weight=2.5, role="hub")

G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4)])
G.add_edge(4, 5, weight=4.2)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())
print("Edges list:", list(G.edges))

try:
    path = nx.shortest_path(G, source=1, target=5)
    print("Shortest path:", path)
except nx.NetworkXNoPath:
    print("No path exists.")

Gra = nx.Graph()
Gra.add_edge(1, 2, color='red', weight=0.84, size=300)
print(Gra[1][2]['size'])
print(Gra.edges[1, 2]['color'])

