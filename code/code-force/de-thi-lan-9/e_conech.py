def solve(n, k, a):
    inf = float('inf')
    dp = [inf] * n
    
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            prev = i - j
            if prev >= 0:
                cost = dp[prev] + abs(a[i] - a[prev])
                if cost < dp[i]:
                    dp[i] = cost
            else:
                break
    return dp[n - 1]
    
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))