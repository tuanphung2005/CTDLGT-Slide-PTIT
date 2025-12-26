def solve(n, s, a):
    c_sum = 0
    left = 0
    c = 0
    for right in range(n):
        c_sum += a[right]
        while c_sum > s:
            c_sum -= a[left]
            left += 1

        c += right - left + 1
    return c
    
n, s = map(int, input().split())
a = list(map(int, input().split()))

print(solve(n, s, a))