def solve(a):
    n = len(a)
    # 1 2 3 4 5
    
    i = n - 2
    while i >= 0 and a[i] > a[i + 1]:
        i -= 1
    if i < 0:
        l = 0
        r = n - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return a

    j = n - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]

    l, r = i + 1, n - 1

    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return a

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(a))