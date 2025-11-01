def solve(n, k, s):

    if k > n or s < 0:
        return 0

    min_sum = 0
    for i in range(1, k + 1):
        min_sum += i

    max_sum = 0
    for i in range(n, n - k, -1):
        max_sum += i

    if s < min_sum or s > max_sum:
        return 0

    dp = []
    for i in range(k + 1):
        dp.append([0] * (s + 1))

    dp[0][0] = 1

    for num in range(1, n + 1):
        upper_j = k
        if num < k:
            upper_j = num
        j = upper_j
        while j >= 1:
            t = s
            while t >= num:
                dp[j][t] = dp[j][t] + dp[j - 1][t - num]
                t -= 1
            j -= 1

    return dp[k][s]

# print(solve(9, 3, 23))
# print(solve(9, 3, 22))
# print(solve(10, 3, 28))
# print(solve(16, 10, 107))
# print(solve(4, 2, 11))

while True:
    num = input().strip().split()

    n = int(num[0])
    k = int(num[1])
    s = int(num[2])

    if n == 0 and k == 0 and s == 0:
        break

    print(solve(n, k, s))
