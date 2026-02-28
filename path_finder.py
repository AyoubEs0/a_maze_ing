from collections import deque


def shortest_path(maze, entry, exit):
    queue = deque([entry])
    visited = set([entry])
    parent = {entry: None}

    directions = [
        ("N", 0, -1, 0),
        ("E", 1, 0, 1),
        ("S", 0, 1, 2),
        ("W", -1, 0, 3)
    ]

    while queue:
        x, y = queue.popleft()

        if (x, y) == exit:
            path = []
            current = exit
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for direction, dx, dy, dir_idx in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < maze.width and 0 <= ny < maze.height:
                if (nx, ny) not in visited:
                    if not maze.walls[y][x][dir_idx]:
                        visited.add((nx, ny))
                        parent[(nx, ny)] = (x, y)
                        queue.append((nx, ny))
    return None
