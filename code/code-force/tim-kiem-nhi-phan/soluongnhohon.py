from bisect import bisect_left

def solve(n, m, a, b):
    res = []
    for i in b:
        idx = bisect_left(a, i)
        res.append(idx)
    return res
    
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*solve(n, m, a, b))