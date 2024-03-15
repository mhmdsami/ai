from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == target:
            return visited, path

        if current not in visited:
            visited.add(current)
            for friend in graph[current]:
                if friend not in visited:
                    queue.append((friend, path + [friend]))

    return None

def dfs(graph, start, target):
    visited = set()
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()

        if current == target:
            return visited, path

        if current not in visited:
            visited.add(current)
            for friend in graph[current]:
                if friend not in visited:
                    stack.append((friend, path + [friend]))

    return None

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Eve': ['Bob'],
    'Frank': ['Charlie']
}

bfs_res = bfs(graph, 'Alice', 'Eve')
print("BFS: ")
if bfs_res:
    bfs_visited, bfs_shortest_path = bfs_res
    print("Visited:", " -> ".join(bfs_visited))
    print("Shortest Path:", " -> ".join(bfs_shortest_path))
else:
    print("No path found")

print()

dfs_res = dfs(graph, 'Alice', 'Eve')
print("DFS: ")
if dfs_res:
    dfs_visited, dfs_shortest_path = dfs_res
    print("Visited:", " -> ".join(dfs_visited))
    print("Shortest Path:", " -> ".join(dfs_shortest_path))
else:
    print("No path found")
