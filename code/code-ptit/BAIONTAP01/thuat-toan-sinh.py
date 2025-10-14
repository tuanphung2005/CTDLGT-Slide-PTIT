def solve(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]

    rec = solve(n - 2)
    res = []
    for s in rec:
        res.append("0" + s + "0")
        res.append("1" + s + "1")
    res.sort()
    return res


n = int(input())
res = solve(n)
for i in res:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()
# print(*(solve(4)))