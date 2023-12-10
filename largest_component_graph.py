def largest_component(graph):
    """Calculate the size of the largest component of the graph."""

    largest = 0
    visited = set()

    for node in graph:
        # size = explore_size_recursive(graph, node, visited)
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size

    return largest


def explore_size_recursive(graph, src, visited):
    """Explore the size from a given node using recursive dfs."""

    if src in visited:
        return 0
    visited.add(src)

    size = 1

    for neighbor in graph[src]:
        size += explore_size_recursive(graph, neighbor, visited)

    return size


def explore_size(graph, src, visited):
    """Explore the size from a given node using dfs."""
    stack = [src]
    size = 0

    while len(stack) > 0:
        print(stack, visited, size)

        current = stack.pop()
        visited.add(current)
        size += 1

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return size


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(largest_component(graph))
