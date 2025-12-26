def solve(n, s, a):
    c_sum = 0
    c_len = 0
    max_len = 0

    
    left = 0
    for right in range(n):
        c_sum += a[right]
        
        while c_sum > s:
            c_sum -= a[left]
            left += 1
        c_len = right - left + 1
        if c_len > max_len:
            max_len = c_len
    return max_len
    
n, s = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, s, a))