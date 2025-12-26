from itertools import combinations

def solve(n, k, a):
    comb = list(combinations(a, k))
    
    res = set()
    for c in comb:
        join = "".join(c)
        res.add(join)
    
    res = sorted(list(res))

    for r in res:
        print(r)

n, k = map(int, input().split())
a = input().split()

solve(n, k, a)