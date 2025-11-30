def selection(n, a):
    for i in range(n - 1):
        minidx = i
        for j in range(i + 1, n):
            if a[i] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
    return a
    
