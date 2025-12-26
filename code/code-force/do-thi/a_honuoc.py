def solve(n, m, k, grid):
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    def dfs(r, c):
        visited[r][c] = True
        area = 1
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= n and 1 <= nc <= m and grid[nr][nc] == 1 and not visited[nr][nc]:
                area += dfs(nr, nc)
        return area
        
    max_lake = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] == 1 and not visited[i][j]:
                max_lake = max(max_lake, dfs(i, j))
    return max_lake

n, m, k = map(int, input().split())
grid = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    grid[x][y] = 1
print(solve(n, m, k, grid))