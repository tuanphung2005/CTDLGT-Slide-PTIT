def solve(n, s, a):
    left = 0
    c_sum = 0
    min_len = float("inf")
    
    for right in range(n):
        c_sum += a[right]
    
        while c_sum >= s:
            c_len = right - left + 1
            if c_len < min_len:
                min_len = c_len
            c_sum -= a[left]
            left += 1
        
    if min_len == float('inf'):
        return -1
    return min_len

n, s = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, s, a))