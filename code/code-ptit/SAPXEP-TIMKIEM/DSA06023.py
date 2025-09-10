def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
        print(f"Buoc {i + 1}: {' '.join(map(str, a))}")
solve()