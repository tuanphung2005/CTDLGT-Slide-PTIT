from itertools import permutations

n, m = map(int, input().split())

others = [i for i in range(1, n + 1) if i != m]

for p in permutations(others):
    print(m, *p)