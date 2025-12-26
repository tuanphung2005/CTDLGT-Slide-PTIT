from bisect import bisect_left, bisect_right
def solve(n, m, a, b):
    
    c = 0
    
    for i in a:
        left = bisect_left(b, i)
        right = bisect_right(b, i)
        c += right - left
    return c
    
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, m, a, b))