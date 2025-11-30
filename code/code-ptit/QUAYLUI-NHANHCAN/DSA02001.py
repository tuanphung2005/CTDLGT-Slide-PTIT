def solve(n, a):
    res = [a]
    current = a[:]
    
    while len(current) > 1:
        next = [current[i] + current[i+1] for i in range(len(current) - 1)]
        res.append(next)
        current = next
    return res


T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    res = solve(n, a)
    for row in res:
        print('[' + ' '.join(map(str, row)) + ']')
