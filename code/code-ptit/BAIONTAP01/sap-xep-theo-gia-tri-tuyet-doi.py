def solve(nums, X):
    arr = {}
    for i in nums:
        abs_num = abs(X - i)
        arr[i] = abs_num

    arr = dict(sorted(arr.items(), key=lambda item: item[1]))
    nums.sort(key=lambda a: abs(X - a))
    return nums

T = int(input())
for _ in range(T):
    n, X = map(int, input().split())
    nums = list(map(int, input().split()))
    res = solve(nums, X)
    print(*res)
    
# print(*(solve([10,5,3,9,2], 7)))
# print(*(solve([1,2,3,4,5], 6)))
    