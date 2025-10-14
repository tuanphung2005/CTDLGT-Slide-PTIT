def check(A, S):
    dp = [False] * (S + 1)
    dp[0] = True
    # print(dp)

    for a in A:
        # print('a=', a)
        for s in range(S, a - 1, -1):
            if dp[s - a] == True:
                dp[s] = True
            # print('s=',s)
            # print(dp)
    
    return dp[S]


T = int(input().strip())
for _ in range(T):
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    if check(A, S):
        print("YES")
    else:
        print("NO")
