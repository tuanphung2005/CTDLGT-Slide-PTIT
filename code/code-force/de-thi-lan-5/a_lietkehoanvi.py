from itertools import permutations

# permutation
def solve(n, m):
    nums = []
    for i in range(1, n + 1):
        if i != m:
            nums.append(i)
    
    perm = list(permutations(nums))
    
    for i in perm:
        print(m, *i)
    
    
    # return nums
n, m = map(int, input().split())
solve(n, m)