T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if flag:
            res.append(a.copy())

    # for i in reversed(res):
    #     print(*i)
    for i in range(len(res) - 1, -1, -1):
        t = i + 1
        print(f'Buoc {t}:', *res[i])