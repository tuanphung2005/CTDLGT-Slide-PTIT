def solve(n, k, a):
    a = sorted(set(a))
    n = len(a)
    res = []
    current = []
    
    def backtrack(start):
        if len(current) == k:
            res.append(list(current))
            return
        for i in range(start, n):
            current.append(a[i])
            backtrack(i + 1)
            current.pop()
    
    backtrack(0)
    return res

# print(*solve(8, 3, [2, 4, 4, 3, 5, 1, 3, 4]))
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = solve(n, k, a)
for i in res:
    print(*i)