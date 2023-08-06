from collections import deque

def find_shortest_path(maze):
    n = len(maze)
    start = None
    end = None

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] != '#'

    def bfs():
        visited = set()
        queue = deque([(start, 0)])

        while queue:
            (x, y), steps = queue.popleft()

            if (x, y) == end:
                return steps

            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), steps + 1))
                    visited.add((new_x, new_y))

        return -1  # No path found

    return bfs()

# Read input
n = int(input())
maze = [input().strip() for _ in range(n)]

# Find and print the shortest path
shortest_path = find_shortest_path(maze)
print(shortest_path)
