def binary(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid + 1
        if arr[left] <= arr[mid]:
            if arr[left] <= x < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < x <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(binary(arr, x))

T = int(input())
for _ in range(T):
    solve()