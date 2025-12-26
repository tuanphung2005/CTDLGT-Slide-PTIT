def solve(n, s, k, a):
    
    min_t = -1
    curr_sum = 0
    for i in range(s - 1, -1, -1):
        curr_sum += a[i]
        if curr_sum <= k:
            min_t = i + 1
        else:
            break
    
    return min_t
t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, s, k, a))