def get_moves(x, y, n, m):
    moves = []
    if x > 0: moves.append((x - 1, y))
    if x < n - 1: moves.append((x + 1, y))
    if y > 0: moves.append((x, y - 1))
    if y < m - 1: moves.append((x, y + 1))

    return moves


n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
alive, damaged, destroyed = 0, 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or visited[i][j]: continue
        stack = [(i, j)]
        ship = []

        while stack:
            x, y = stack.pop()
            ship.append((x, y))
            for next_x, next_y in get_moves(x, y, n, m):
                if grid[next_x][next_y] == '.' or visited[next_x][next_y]: continue
                stack.append((next_x, next_y))
                visited[next_x][next_y] = True

        if all(grid[x][y] == '#' for x, y in ship): alive += 1
        elif all(grid[x][y] == 'X' for x, y in ship): destroyed += 1
        else: damaged += 1

print(alive, damaged, destroyed)
