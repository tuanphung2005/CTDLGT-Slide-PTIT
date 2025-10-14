T = int(input())


for _ in range(T):
    nA, nB = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    union = list(set(A) | set(B))
    intersection = list(set(A) & set(B))
    print(*union)
    print(*intersection)


    # TLE
    # union = []
    # for i in A:
    #     if i not in union:
    #         union.append(i)
    # for i in B:
    #     if i not in union:
    #         union.append(i)
    # print(*union)

    # intersection = []
    # for i in A:
    #     if i in B and i not in intersection:
    #         intersection.append(i)
    # print(*intersection)
