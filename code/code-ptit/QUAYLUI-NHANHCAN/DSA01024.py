def solve(n, k, arr):
    temp = sorted(set(arr))

    n = len(temp)
    current = []
    res = []

    def backtrack(start):
        if len(current) == k:
            res.append(' '.join(current))
            return
        for i in range(start, n):
            current.append(temp[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return res

n, k = map(int, input().split())
arr = list(map(str, input().split()))
res = solve(n, k, arr)
for i in res:
    print(i)

