def solve(n, m, a):
    dp = [0] * (m + 1)
    for w, v in a:
        for i in range(m, w - 1, -1):
            if dp[i - w] + v > dp[i]:
                dp[i] = dp[i - w] + v
    return dp[m]

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print(solve(n, m, a))
