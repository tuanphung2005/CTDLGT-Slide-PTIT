def solve(n, a):
    
    res = []
    
    def backtrack(i, temp):
        if len(temp) >= 2:
            res.append(temp.copy())
        for j in range(i, n):
            if not temp or a[j] > temp[-1]:
                temp.append(a[j])
                backtrack(j + 1, temp)
                temp.pop()
    backtrack(0, [])
    res1 = []
    for i in res:
        res1.append(" ".join(map(str, i)))
    res1.sort()
    return "\n".join(res1)
# res = solve(4, [6, 3, 7, 11])
# print(res)
n = int(input())
print(solve(n, list(map(int, input().split()))))