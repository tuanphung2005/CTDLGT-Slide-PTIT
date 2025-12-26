def solve(n, k):
    
    f = ['A', 'B']

    if n == 0:
        if k == 1:
            return 1
    if n == 1:
        if k == 1:
            return 0

    count = 0
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    
    for i in range(k):
        if f[n - 1][i] == 'A':
            count += 1

    return count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
