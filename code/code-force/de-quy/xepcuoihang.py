from itertools import permutations
def solve(n, a, name):
    a.sort()
    
    perm = list(permutations(a))
    for i in range(len(perm)):
        if perm[i][-1] == name:
            print(*perm[i])
    return 

# n = 4
# a = ["dong", "tay", "nam", "bac"]
# name = "nam"

n = int(input())
a = input().split()
name = input()

solve(n, a, name)