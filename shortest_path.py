def shortest_path(graph, src, dst):

    visited = set()
    visited.add(src)
    queue = [(src, 0)]

    while len(queue) > 0:

        (current, dist) = queue.pop(0)
        if current == dst:
            return dist

        for neighbor in graph[current]:
            if neighbor[0] not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return None


def edges_to_graph(edges):
    """Convert edges to adjacency info."""
    graph = {}

    for (a, b) in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]
graph = edges_to_graph(edges)
print(shortest_path(graph, 'j', 'm'))
print(shortest_path(graph, 'i', 'n'))
