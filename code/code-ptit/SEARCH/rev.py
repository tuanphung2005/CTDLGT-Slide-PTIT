def interpolation(a, x):
    l = 0
    r = len(a) - 1
    while l <= r and a[l] <= x <= a[r]:
        m = l + (x - a[l]) * (r - l) // (a[l] - a[r])
        
        if a[m] < x:
            m = l + 1
        elif a[m] > x:
            m = r - 1
        else:
            return m
    return -1
    
def binary(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            m = l + 1
        elif a[m] > x:
            m = r - 1
    return -1
    
    
def fibsearch(a, x):
    n = len(a)
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    k = len(fib)
    inf = pos = 0
    while k >= 0:
        if k >= 2:
            pos = inf + fib[k - 2]
        else:
            pos = inf
        
        if pos >= n or x < a[pos]:
            k -= 1
            
        elif x > a[pos]:
            k -= 2
            inf = pos + 1
        else:
            return pos
            
    return -1