def print_dfs(graph, source):
    """Traverse and print all nodes in dfs."""

    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def print_dfs_recursive(graph, source):
    """Traverse and print all nodes in recursive dfs."""

    print(source)

    for neighbor in graph[source]:
        print_dfs_recursive(graph, neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

print_dfs(graph, 'a')
print("\n")
print_dfs_recursive(graph, 'a')
