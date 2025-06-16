maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

visited = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

row = len(maze)
col = len(maze[0])

start = [0, 0]
end = [row - 1, col - 1]

def AllPath(start, end, p, ans, visited):
    x, y = start

    # Base case: out of bounds or obstacle or already visited
    if x < 0 or y < 0 or x >= row or y >= col:
        return
    if maze[x][y] == 1 or visited[x][y] == 1:
        return

    # Destination reached
    if x == end[0] and y == end[1]:
        ans.append(p)
        return

    # Mark visited
    visited[x][y] = 1

    # Move in all four directions
    AllPath([x, y - 1], end, p + "L", ans, visited)
    AllPath([x, y + 1], end, p + "R", ans, visited)
    AllPath([x - 1, y], end, p + "U", ans, visited)
    AllPath([x + 1, y], end, p + "D", ans, visited)

    # Backtrack
    visited[x][y] = 0

ans = []
AllPath(start, end, "", ans, visited)
print(ans)
