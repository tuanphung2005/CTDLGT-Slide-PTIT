T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    dict = {}
    for i in a:
        dict[i] = dict.get(i, 0) + 1

    print(dict.get(x, -1))