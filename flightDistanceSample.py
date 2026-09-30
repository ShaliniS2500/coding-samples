import random
import scipy.sparse as sparse
import numpy as np


num_cities = 500
cities_matrix = sparse.random(num_cities, num_cities, density=0.01, format='coo')

edges = []
for u, v, weight in zip(cities_matrix.row, cities_matrix.col, cities_matrix.data):
    if u != v:
        edges.append((int(u), int(v), int(weight*100)))


def check_chunk(chunk, dists):
    for city1, city2, time in chunk:
        if dists[city1] != float('inf'):
            if dists[city1] + time < dists[city2]:
                dists[city2] = dists[city1] + time


test_chunk = [
    (0, 1, 10),
    (1, 2, 5),
    (0, 2, 20)
]

mock_dists = [0, float('inf'), float('inf')]

print(f"REAL GRAPH DATA SEED: Generated {len(edges)} total flights.")
print("START DISTANCES:", mock_dists)

check_chunk(test_chunk, mock_dists)
print("ROUND 1 DISTANCES:", mock_dists)

check_chunk(test_chunk, mock_dists)
print("ROUND 2 DISTANCES:", mock_dists)

