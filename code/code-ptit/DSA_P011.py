# AC
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(input()))

visited = [[False]*M for _ in range(N)]

def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '#' and not visited[nx][ny]:
                dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '#' and not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)