def solve(n, m):
    # n -> m, n * 2 | n - 1
    # m / 2 | m + 1
    c = 0
    
    while n != m:
        if m > n:
            if m % 2 == 0:
                m /= 2
            else:
                m += 1
                m /= 2
                c += 1
                
            c += 1
            
        elif n > m:
            n -= 1
            c += 1
            
    
    return c
n, m = map(int, input().split())

print(solve(n, m))