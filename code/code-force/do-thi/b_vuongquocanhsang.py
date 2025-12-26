def dfs(n, adj):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            stack = [i]
            visited [i] = True
            while stack:
                u = stack.pop()
                for v in range(n):
                    if adj[u][v] == 1 and not visited[v]:
                        visited[v] = True
                        stack.append(v)
    return count

def solve(n, adj):
    so_bang_dau = dfs(n, adj)
    
    so_cau = 0
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j] == 1:
                adj[i][j] = 0
                adj[j][i] = 0
                
                if dfs(n, adj) > so_bang_dau:
                    so_cau += 1
                
                adj[i][j] = 1
                adj[j][i] = 1
    return so_cau

n = int(input())
adj = []
for i in range(n):
    adj.append(list(map(int, input().split())))
print(solve(n, adj))