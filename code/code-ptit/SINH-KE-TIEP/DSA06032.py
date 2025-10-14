def solve(nums, k):
    nums.sort()
    n = len(nums)
    count = 0
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < k:
                count += right - left
                left += 1
            else:
                right -= 1
    
    return count

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums, k))