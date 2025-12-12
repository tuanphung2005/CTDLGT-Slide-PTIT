def solve(n, a, k):
    a.sort()
    res = []
    
    temp = []
    def backtrack(i, sum):
        if sum == k:
            res.append(temp.copy())
            return
        if i == n:
            return
        temp.append(a[i])
        backtrack(i + 1, sum + a[i])
        temp.pop()
        backtrack(i + 1, sum)
        
    backtrack(0, 0)
    if not res:
        return -1
    else:
        output = ""
        for s in res:
            output += "[" + " ".join(map(str, s)) + "] "
        return output.strip()

# print(solve(5, [5, 10, 15, 20, 25], 50))
# print(solve(8, [15, 22, 14, 26, 32, 9, 16, 8], 53))

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    print(solve(n, a, k))