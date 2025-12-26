from itertools import permutations

def solve(n):
    
    num_list = list(range(1, n + 1))
    perm = list(permutations(num_list))
    
    def dif(a):
        s = 0
        for i in range(1, len(a)):
            s += a[i - 1] - a[i]
        if s > 0:
            return True
        return False
    
    for i in range(len(perm)):
        if dif(perm[i]):
            print(*perm[i],'')
    
    return
n = int(input())
solve(n)