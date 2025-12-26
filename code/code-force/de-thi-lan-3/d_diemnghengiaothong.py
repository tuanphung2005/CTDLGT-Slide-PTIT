def dfs(start, end, n, adj, hidden_node):

    visited = [False] * (n + 1)
    visited[hidden_node] = True

    if visited[start]:
        return False

    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()

        if u == end:
            return True

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return False

def solve(n, m, x, y, a):

    adj= [[] for _ in range(n + 1)]

    for i in range(m):
        u = a[i][0]
        v = a[i][1]
        adj[u].append(v)

    res = 0
    for i in range(1, n + 1):
        if i == x or i == y:
            continue

        if not dfs(x, y, n, adj, i):
            res += 1
        
    return res

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    print(solve(n, m, x, y, a))