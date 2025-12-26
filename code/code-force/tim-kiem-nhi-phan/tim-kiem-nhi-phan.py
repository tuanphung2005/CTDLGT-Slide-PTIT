from bisect import bisect_left, bisect_right

def solve(n, t, x, a):
    
    res = []
    
    if t == 1:
        idx = bisect_left(a, x)
        if idx < n and a[idx] == x:
            res.append("YES")
        else:
            res.append("-1")
    if t == 2:
        idx = bisect_left(a, x)
        if idx < n and a[idx] == x:
            res.append(str(idx + 1))
        else:
            res.append("-1")
            
    if t == 3:
        idx = bisect_right(a, x)
        idx -= 1
        if idx < n and a[idx] == x:
            res.append(str(idx + 1))
        else:
            res.append(-1)
            
    return res

n, q = map(int, input().split())

a = list(map(int, input().split()))
for i in range(q):
    t, x = map(int, input().split())
    print(*solve(n, t, x, a))
            
        