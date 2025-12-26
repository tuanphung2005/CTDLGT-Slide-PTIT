F = [0] * 46
A = [0] * 46

F[0] = 1; A[0] = 1
F[1] = 1; A[1] = 0

for i in range(2, 46):
    F[i] = F[i-1] + F[i-2]
    A[i] = A[i-1] + A[i-2]

def solve(n, k):
    if n == 0: return 1
    if n == 1: return 0

    if k == F[n]: return A[n]

    len_left = F[n-1]
    
    if k <= len_left:
        return solve(n-1, k)
    else:
        return A[n-1] + solve(n-2, k - len_left)

try:
    T_str = input()
    if T_str:
        T = int(T_str)
        for _ in range(T):
            line = input().split()
            if line:
                n, k = map(int, line)
                print(solve(n, k))
except:
    pass