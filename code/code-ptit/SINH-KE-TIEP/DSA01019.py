def solve(n):
    s = [''] * n
    res = []

    def backtrack(i):
        if i == n:
            res.append(''.join(s))
            return

        for ch in ['A', 'H']:
            if i == 0 and ch != 'H':
                continue
            if i == n - 1 and ch != 'A':
                continue
            if i > 0 and s[i - 1] == 'H' and ch == 'H':
                continue

            s[i] = ch
            backtrack(i + 1)

    backtrack(0)
    return res

# print(*solve(6))
T = int(input())
for _ in range(T):
    n = int(input())
    res = solve(n)
    for i in res:
        print(i)