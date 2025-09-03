# SIEVE OF ERATOSTHENES
MAX = 10**6 + 1

is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False

def solve(n):
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            return
    print(-1)

T = int(input())
for _ in range(T):
    n = int(input())
    solve(n)