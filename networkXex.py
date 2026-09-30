import networkx as nx
import matplotlib.pyplot as plt
import math

# G = nx.complete_graph(12)
# nx.draw(G)
# plt.show()
#
# G_1 = nx.Graph()
# e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
# G_1.add_weighted_edges_from(e)
# print(nx.dijkstra_path(G_1, 'a', 'd'))

# G = nx.diamond_graph()
# subax1 = plt.subplot(121)
# nx.draw(G)
# subax2 = plt.subplot(423)
# nx.draw(G, pos=nx.circular_layout(G), node_color='g', edge_color='r')
# plt.show()


G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)
G.add_edge('y', 'x', function=math.cos)
G.add_node(math.cos)
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)
print(G)


