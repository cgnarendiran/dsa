def has_path_bfs(graph, src, dst):
    """Check if src to dst has a path in the graph using bfs."""

    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)

        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            queue.append(neighbor)

    return False


def has_path_dfs(graph, src, dst):
    """Check if src to dst has a path in the graph using dfs."""

    stack = [src]

    while len(stack) > 0:
        current = stack.pop()

        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            stack.append(neighbor)

    return False


def has_path_dfs_recursive(graph, src, dst):
    """Check if src to dst has a path in the graph using recursive dfs."""

    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path_dfs_recursive(graph, neighbor, dst):
            return True

    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': [],
}

print(has_path_bfs(graph, 'f', 'k'))
print(has_path_dfs(graph, 'f', 'k'))
print(has_path_dfs_recursive(graph, 'f', 'k'))
