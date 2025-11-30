t = int(input())
for _ in range(t):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    
    paths = []
    
    def dfs(i, j, s):
        if i == N-1 and j == N-1:
            paths.append(s)
            return
        
        # d
        if i+1 < N and A[i+1][j] == 1:
            dfs(i+1, j, s + "D")
        
        # r
        if j+1 < N and A[i][j+1] == 1:
            dfs(i, j+1, s + "R")
    
    if A[0][0] == 1:
        dfs(0, 0, "")
    
    if len(paths) == 0:
        print(-1)
    else:
        print(" ".join(paths))
