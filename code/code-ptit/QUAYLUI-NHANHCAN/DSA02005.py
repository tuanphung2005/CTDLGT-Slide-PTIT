def solve(s):

    chars = sorted(s)
    n = len(chars)
    used = [False]*n
    cur = []
    res = []

    def backtrack():
        if len(cur) == n:
            res.append(''.join(cur))
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            cur.append(chars[i])
            backtrack()
            cur.pop()
            used[i] = False

    backtrack()
    return res

# --- đọc input và xuất ---
T = int(input().strip())
for _ in range(T):
    s = input().strip()
    ans = solve(s)
    print(' '.join(ans))
