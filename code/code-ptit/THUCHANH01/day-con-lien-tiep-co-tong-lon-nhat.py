def solve(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            max_sum = max(max_sum, sum)
    return max_sum

# print(solve([-2, -5, 6, -2, -3, 1, 5, -6]))

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))