# TLE
def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))

        adj = [[] for _ in range(n + 1)]
        for i in range(0, 2*m, 2):
            u = arr[i]
            v = arr[i+1]
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)

        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)

        comp = 0
        for i in range(1, n + 1):
            if not visited[i]:
                comp += 1
                dfs(i)

        print(comp)

solve()
