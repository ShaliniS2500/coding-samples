import matplotlib.pyplot as plt
import networkx as nx

# Define the 12 chromatic scale names
pitch_names = [
    'C',
    'C#',
    'D',
    'D#',
    'E',
    'F',
    'F#',
    'G',
    'G#',
    'A',
    'A#',
    'B',
]

G = nx.Graph()
pos = {}

grid_min, grid_max = -1, 3

for x in range(grid_min, grid_max):
    for y in range(grid_min, grid_max):
        semitones = (7 * x + 4 * y) % 12
        note_name = pitch_names[semitones]

        node_id = (x, y)
        pos[node_id] = (x + 0.5 * y, y)
        G.add_node(node_id, label=note_name)

for n1 in G.nodes:
    for n2 in G.nodes:
        if n1 != n2:
            x1, y1 = n1
            x2, y2 = n2
            dx, dy = x2 - x1, y2 - y1

            if (abs(dx) == 1 and dy == 0) or (dy == 1 and dx == 0) or (dx == -1 and dy == 1) or (dx == 1 and dy == -1):
                G.add_edge(n1, n2)

labels = nx.get_node_attributes(G, 'label')

plt.figure(figsize=(9, 8))
nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_size=1100,
    node_color='lightgreen',
    edge_color='black',
    font_size=10,
    font_weight='bold',
)

plt.title('2D Tonnetz Lattice (All 12 Pitches with Repeats)', fontsize=14)
plt.axis('off')
plt.show()
