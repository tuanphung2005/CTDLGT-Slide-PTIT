def interpolation(a, x):
    l, r = 0, len(a) - 1
    
    while l <= r and a[l] <= x <= a[r]:
            mid = l + (x - a[l]) * (r - l) // (a[r] - a[l])
            
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
    return -1

def binary(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        if a[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
def fibsearch(A, x):
    n = len(A)
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    k = len(fib) - 1
    inf = 0
    pos = 0
    
    while k >= 0:
        if k >= 2:
            pos = inf + fib[k-2]
        else:
            pos = inf
        if pos >= n or x < A[pos]:
            k -= 1
        elif x > A[pos]:
            inf = pos + 1
            k -= 2
        else:
            return pos
    return -1
