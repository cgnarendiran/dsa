def has_path_undirected(edges, src, dst):
    """Check if there's a path b/w src and dst in undirected graph."""

    graph = edges_to_graph(edges)
    visited = set()
    # return dfs_recursive(graph, src, dst, visited)
    return dfs(graph, src, dst, visited)


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


def dfs_recursive(graph, src, dst, visited):
    """Traverse the graph using recursive dfs"""

    if src in visited:
        return False
    visited.add(src)

    if src == dst:
        return True

    for neighbor in graph[src]:
        if dfs_recursive(graph, neighbor, dst, visited):
            return True

    return False


def dfs(graph, src, dst, visited):
    """Traverse the graph using dfs"""

    stack = [src]
    visited.add(src)

    while len(stack) > 0:
        current = stack.pop()
        if current == dst:
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return False


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

print(has_path_undirected(edges, 'j', 'm'))
print(has_path_undirected(edges, 'i', 'n'))
