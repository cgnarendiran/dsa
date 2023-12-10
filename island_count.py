def island_count(grid):
    """Count the number of islands of this grid."""

    graph = grid_to_graph(grid)
    print(graph)

    visited = set()
    count = 0

    for node in graph:
        if dfs(graph, node, visited):
            count += 1

    return count


def dfs(graph, node, visited):
    """Traverse the graph using dfs."""

    if node in visited:
        return False
    visited.add(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

    return True


def grid_to_graph(grid):
    """Convert a grid to adjacency graph."""
    graph = {}

    for r, full_row in enumerate(grid):
        for c, value in enumerate(full_row):
            if value == '1':
                graph[(r,c)] = []
                for pos in [(r-1,c), (r+1,c), (r,c-1), (r, c+1)]:
                    if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == '1':
                        graph[(r,c)].append(pos)

    return graph


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(island_count(grid))
