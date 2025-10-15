#TODO: TLE
def solve(nums):
    return sorted(nums)

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    print(*solve(nums))