# def mazeTwoMoves(maze, start, end, p, ans):
#     rows, cols = end[0], end[1]
#     i, j = start

#     # Check if out of bounds or hitting a blocked cell (0 now means blocked)
#     if i > rows or j > cols or maze[i][j] == 0:
#         return

#     if i == rows and j == cols:
#         ans.append(p)
#         return
#     # Move Down
#     mazeTwoMoves(maze, [i + 1, j], end, p + "D", ans)
#     # Move Right
#     mazeTwoMoves(maze, [i, j + 1], end, p + "R", ans)
#     # Move Diagonal
#     mazeTwoMoves(maze, [i + 1, j + 1], end, p + "K", ans)

def mazeTwoMoves(maze, start, end, p, ans, visited):
    rows, cols = end[0], end[1]
    i, j = start

    if i > rows or j > cols or i < 0 or j < 0:
        return
    if maze[i][j] == 0 or visited[i][j] == 1:
        return

    if i == rows and j == cols:
        ans.append(p)
        return

    visited[i][j] = 1

    mazeTwoMoves(maze, [i + 1, j], end, p + "D", ans, visited)
    mazeTwoMoves(maze, [i, j + 1], end, p + "R", ans, visited)
    mazeTwoMoves(maze, [i, j - 1], end, p + "L", ans, visited)
    mazeTwoMoves(maze, [i - 1, j], end, p + "U", ans, visited)

    visited[i][j] = 0



# Example usage
maze = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

ans = []
visited = [[0 for j in i] for i in maze ]
print(visited)
mazeTwoMoves(maze, [0, 0], [2, 2], "", ans, visited)
print("All paths:", ans)
