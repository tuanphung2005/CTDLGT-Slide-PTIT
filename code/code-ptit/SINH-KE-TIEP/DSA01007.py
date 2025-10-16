def solve(n):
    s = [''] * n
    res = []

    def backtrack(i):
        if i == n:
            res.append(''.join(s))
            return
        for ch in ['A', 'B']:
            s[i] = ch
            backtrack(i + 1)
    
    backtrack(0)
    return res

# print(solve(2))

T = int(input())
for _ in range(T):
    n = int(input())
    res = solve(n)
    for i in res:
        print(i, end=' ')
    print()