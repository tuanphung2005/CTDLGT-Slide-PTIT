# TODO: WRONG ANSWER
def ss(a, b, x):
    da, db = abs(a - x), abs(b - x)
    if da != db:
        return da < db
    return a < b

def merge_sort(arr, x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], x)
    right = merge_sort(arr[mid:], x)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if ss(left[i], right[j], x):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

T = int(input())
for _ in range(T):
    n_x = input().split()
    while len(n_x) < 2:
        n_x += input().split()
    n, x = map(int, n_x)
    arr = list(map(int, input().split()))

    arr = merge_sort(arr[:n], x)
    for num in arr:
        print(num, end=' ')
    print()