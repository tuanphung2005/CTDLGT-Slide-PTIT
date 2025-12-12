def solve(n):
    count = 0 
    
    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    
    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return

        for c in range(n):
            
            idiag1 = r + c
            idiag2 = r - c + n - 1

            if not col[c] and not diag1[idiag1] and not diag2[idiag2]:

                col[c] = True
                diag1[idiag1] = True
                diag2[idiag2] = True

                backtrack(r + 1)

                col[c] = False
                diag1[idiag1] = False
                diag2[idiag2] = False
                
    backtrack(0)
    return count 
T = int(input())
for _ in range(T):
    print(solve(int(input())))
