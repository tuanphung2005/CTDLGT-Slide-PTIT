def solve(n):
    if n == 0:
        return [""]

    rec = solve(n - 1)
    res = []
    for s in rec:
        res.append(s + "A")
        res.append(s + "B")
    return res
    
T = int(input())
for _ in range(T):
    n = int(input())
    print(" ".join(solve(n)))

# print(*(solve(2)))