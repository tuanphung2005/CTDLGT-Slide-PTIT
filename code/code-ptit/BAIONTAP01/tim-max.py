def solve(nums):
    mod = 10**9 + 7
    nmax = 0
    nums.sort()
    for i in range(1, len(nums)):
        nmax += (nums[i] * i % mod) % mod
    return nmax

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    res = solve(nums)
    print(res)

# print(solve([1, 2, 3]))
# print(solve([5, 3, 2, 4, 1]))