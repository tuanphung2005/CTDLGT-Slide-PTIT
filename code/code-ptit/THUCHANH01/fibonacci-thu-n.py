MOD = 1000000007

def fib(n):
    if n == 0:
        return 0, 1
    a, b = fib(n // 2)
    diff = (2 * b - a) % MOD
    c = (a * diff) % MOD
    d = (a * a + b * b) % MOD
    if n % 2 == 1:
        return d, (c + d) % MOD
    return c, d

T = int(input())
for _ in range(T):
    n = int(input())
    print(fib(n)[0] % MOD)