def dfs (start, adj, visited):
    
    size = 0
    
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        size += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return size
    
def solve(n, m, a):
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = a[i][0]
        v = a[i][1]
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    
    size1 = dfs(1, adj, visited)
    
    size_other = 0
    for i in range(2, n + 1):
        if not visited[i]:
            temp = dfs(i, adj, visited)
            if temp > size_other:
                size_other = temp
    return size1 + size_other
    
n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
print(solve(n, m, a))