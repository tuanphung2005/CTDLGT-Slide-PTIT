
def solve(n, m, a):
    deg = [0] * (n + 1)
    for u, v in a:
        deg[v] += 1
    
    ans = 0

    for i in range(1, n + 1):
        if deg[i] == 0:
            ans += 1

    if ans == 0 and n > 0:
        return 1
    return ans

n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

print(solve(n, m, a))