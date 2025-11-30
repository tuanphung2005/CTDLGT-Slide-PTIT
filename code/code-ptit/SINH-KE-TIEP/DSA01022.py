def solve(n, a):
    
    r = 1
    for i in range(n):
        c = 0
        for j in range(i + 1, n):
            if a[j] < a[i]:
                c += 1
        r += c * fact(n - i - 1)
    return r
    
    return 0

def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))