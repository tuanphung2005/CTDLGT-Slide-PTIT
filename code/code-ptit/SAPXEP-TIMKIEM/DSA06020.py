
def binary_search(arr, X):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == X:
            return True
        elif arr[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return False

def solve():
    n, X = map(int, input().split())
    arr = list(map(int, input().split()))

    if binary_search(arr, X):
        print(1)
    else:
        print(-1)

T = int(input())
for _ in range(T):
    solve()