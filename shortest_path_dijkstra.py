import heapq

def shortest_path(graph, src, dst):
    visited = set()
    queue = [(0, src)]  # Priority queue, with distance as the first element

    while queue:
        dist, current = heapq.heappop(queue)
        if current == dst:
            return dist
        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (dist + weight, neighbor))

    return None

def edges_to_graph_weighted(edges):
    """Convert edges with weights to adjacency info."""
    graph = {}

    for (a, b, weight) in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append((b, weight))
        graph[b].append((a, weight))

    return graph

# Example edges with weights
edges = [
    ('i', 'j', 2),
    ('k', 'i', 1),
    ('m', 'k', 3),
    ('k', 'l', 4),
    ('o', 'n', 5),
]

graph = edges_to_graph_weighted(edges)
print(shortest_path_dijkstra(graph, 'j', 'm'))
