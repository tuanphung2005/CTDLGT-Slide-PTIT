def solve(n, k, nums):
    i = k - 1
    while i >= 0:
        if nums[i] < n - (k - 1 - i):
            nums[i] += 1
            for j in range(i + 1, k):
                nums[j] = nums[j - 1] + 1
            return nums
        i -= 1
    return list(range(1, k + 1))

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    result = solve(n, k, nums)
    print(*result)