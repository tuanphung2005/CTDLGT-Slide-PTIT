def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        check = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                check = True
        if check:
            print(f"Buoc {i + 1}: {' '.join(map(str, arr))}")
        else:
            break

n = int(input())
a = list(map(int, input().split()))
bubble_sort(a)