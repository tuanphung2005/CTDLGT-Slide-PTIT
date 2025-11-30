def bubble(n, a):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a