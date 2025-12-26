def solve(n, a):
    a.sort()

    num1 = 0
    num2 = 0

    for i in range(n):
        if i % 2 == 0:
            num1 = num1 * 10 +a[i]
        else:
            num2 = num2 * 10 + a[i]
    return num1 + num2

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solve(n, a))