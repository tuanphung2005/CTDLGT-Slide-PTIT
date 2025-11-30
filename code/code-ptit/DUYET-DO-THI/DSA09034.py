def solve(N, M, grid):
    visited = [[False]*M for _ in range(N)]

    dx = [-1,-1,-1, 0,0, 1,1,1]
    dy = [-1, 0, 1,-1,1,-1,0,1]

    def dfs(x, y):
        visited[x][y] = True
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == 'W':
                    dfs(nx, ny)

    c = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W' and not visited[i][j]:
                c += 1
                dfs(i, j)

    return c

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().strip()))
print(solve(N, M, grid))
