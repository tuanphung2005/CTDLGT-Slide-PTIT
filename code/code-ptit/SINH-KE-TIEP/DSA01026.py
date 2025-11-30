def solve(n):
    res = []
    def backtrack(s):
        if len(s) == n:
            if s[-1] == '6':
                # print(s)
                res.append(s)
            return

        for ch in '68':
            if len(s) == 0:
                if ch == '8':
                    backtrack(s + ch)
                continue

            if len(s) >= 1 and s[-1] == '8' and ch == '8':
                continue

            if len(s) >= 3 and s[-1] == s[-2] == s[-3] == '6' and ch == '6':
                continue

            if len(s) == n - 1 and ch != '6':
                continue

            backtrack(s + ch)

    backtrack("")
    return res
    
n = int(input())
res = solve(n)
for i in res:
    print(i)