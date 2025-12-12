def solve(M, N):

    def backtrack(i, j):
        if i >= M or j >= N:
            return 0

        if i == M - 1 and j == N - 1:
            return 1
        down = backtrack(i + 1, j)
        right = backtrack(i, j + 1)
        
        return down + right

    return backtrack(0, 0)

T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    for i in range(M):
        A = list(map(int, input().split()))
    
    print(solve(M, N))