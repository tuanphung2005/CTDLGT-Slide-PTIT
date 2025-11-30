def solve(n):
    a = list(range(n, 0, -1))
    res = []
    while True:
        res.append(''.join(map(str, a)))
        i = n - 2
        while i >= 0 and a[i] < a[i + 1]:
            i -= 1
        if i < 0:
            break
        j = n - 1
        while a[j] > a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
        
        left, right = i + 1, n - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    return res


T = int(input())
for _ in range(T):
    n = int(input())
    print(*solve(n))
