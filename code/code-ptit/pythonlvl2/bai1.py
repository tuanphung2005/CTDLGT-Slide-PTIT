def selection(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = selection(nums)
    total = 0
    for i in range(1, n):
        if i % m == 0:
            total += nums[i]
    print(total)