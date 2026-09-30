from collections import deque

def has_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True

    return False

def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge


        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1

    return count

def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

def largest_component(graph):
    visited = set()

    largest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size

    return largest

def explore_size(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)

    return size

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited  = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count

def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False

    if grid[r][c] == 'W':
        return False

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True

grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(island_count(grid))