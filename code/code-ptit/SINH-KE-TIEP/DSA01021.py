def solve(k, a):
    
    i = k - 1
    pos = -1
    while i >= 0:
        if a[i] < n - (k - i - 1):
            pos = i
            break
        i -= 1
    
    if pos == -1:
        return k
        
    
    b = [0] * k
    for i in range(k):
        b[i] = a[i]
        
    b[pos] += 1
    for i in range(pos + 1, k) :
        b[i] = b[i - 1] + 1
        
    c = 0
    for i in range(k):
        x = b[i]
        flag = False
        for j in range(k):
            if a[j] == x:
                flag = True
                break
        if not flag:
            c += 1
    return c

    
T = int(input())


for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(k, a))
    