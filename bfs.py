def print_bfs(graph, source):
    """Traverse and print all nodes in bfs."""

    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

print_bfs(graph, 'a')
