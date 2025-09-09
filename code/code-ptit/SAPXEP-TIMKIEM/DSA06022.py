def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if len(a) < 2:
        return -1
    min1 = float('inf')
    min2 = float('inf')
    for i in a:
        if i < min1:
            min2 = min1
            min1 = i
        elif min1 < i < min2:
            min2 = i
    if min1 == float('inf') or min2 == float('inf'):
        return -1
    return min1, min2

T = int(input())
for _ in range(T):
    res = solve()
    if res == -1:
        print(res)
    else:
        print(res[0], res[1])