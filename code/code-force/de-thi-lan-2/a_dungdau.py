from itertools import permutations
def solve(n, names, selected):
    temp = []
    for i in names:
        if i != selected:
            temp.append(i)
            
    temp.sort()
    perm = list(permutations(temp))
    
    
    for i in perm:
        print(selected, *i)
    
    
    return perm
    
n = int(input())
a = input().split()
selected = input()
solve(n, a, selected)