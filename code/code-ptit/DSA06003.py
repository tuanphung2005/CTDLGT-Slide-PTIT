# TODO: TLE

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    print(swaps)