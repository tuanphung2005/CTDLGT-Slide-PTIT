def solve(n, s, a):
    
    left = 0
    c_sum = 0
    res = 0
    for right in range(n):
        c_sum += a[right]
        
        while c_sum >= s:
            res += (n - right)
            c_sum -= a[left]
            left += 1
    
    return res
    
n, s = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, s, a))
    
