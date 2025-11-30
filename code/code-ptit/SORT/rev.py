def selection(a, n):
    for i in range(n - 1):
        minidx = 0
        for j in range(i + 1, n):
            if a[i] > a[j]:
                minidx = j
        a[minidx], a[i] = a[i], a[minidx]
    return a
    
def insertion(a, n):
    for i in range(n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def part(a, l, h):
    pivot = a[h]
    i = l - 1
    for j in range(l, h):
        if a[j] <= pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i + 1], a[h] = a[h], a[i + 1]
    return i + 1
def qsort(a, l, h):
    if l < h:
        p = part(a, l, h)
        qsort(a, l, p - 1)
        qsort(a, p + 1, h)

def mege(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = a[l + i]
    for j in range(n2):
        L[j] = a[m + j + 1]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[i]
            j += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
def msort(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        msort(a, l, m)
        msort(a, m + 1, l)
        mege(a, l, m, r)
            