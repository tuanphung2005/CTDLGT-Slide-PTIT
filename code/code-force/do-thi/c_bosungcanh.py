def dsf(start, adj, visited):
    nodes = []
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        
        nodes.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return nodes
    
def solve(n, m, adj):
    visited = [False] * (n + 1)
    all = []
    for i in range(1, n + 1):
        if not visited[i]:
            component = dsf(i, adj, visited)
            all.append(component)
            
    size1 = 0
    size = []
    for comp in all:
        if 1 in comp:
            size1 = len(comp)
        else:
            size.append(len(comp))
    if not size:
        return size1
    return size1 + max(size)
    
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
print(solve(n, m, adj))
    