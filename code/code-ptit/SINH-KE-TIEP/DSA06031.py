def solve(nums, k):
    dq = []
    res = []
    
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.pop(0)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    
    return res

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(*solve(nums, k))