def solve(n, k):
    chars = [chr(i) for i in range(ord('A'), ord('A') + n)]
    current = []
    
    res = []
    def backtrack(start):
        if len(current) == k:
            res.append(''.join(current))
            return
        for i in range(start, n):
            current.append(chars[i])
            backtrack(i + 1)
            current.pop()
    backtrack(0)
    return res

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    res = solve(n, k)
    for i in res:
        print(i)