def solve(n, s, m):
    # res = s * m
    # dopen = 0
    # for i in range(s):
    #     day = (2 + i) % 7
    #     if day != 0:
    #         dopen += 1
    # max = dopen * n
    # if res > max:
    #     return -1
    # return (res + n - 1) // n

    total = s * m
    if n < m:
        return -1
    
    chunhat = s // 7
    dopen = s - chunhat

    dneed = total // n
    if total % n != 0:
        dneed += 1

    if dneed > dopen:
        return -1
    return dneed

# print(solve(16, 10, 2))
# print(solve(20, 10, 30))

T = int(input())
for _ in range(T):
    n, s, m = map(int, input().split())
    print(solve(n, s, m))