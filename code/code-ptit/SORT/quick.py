def part(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def qsort(a, low, high):
    if low < high:
        p = part(a, low, high)
        qsort(a, low, p - 1)
        qsort(a, p + 1, high)
