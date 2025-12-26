def solve(n, m, a, b):
    res_val = []
    res_str = []
    
    i = 0
    j = 0
    
    while i < n and j < m:
        if a[i] <= b[j]:
            res_val.append(str(a[i]))
            res_str.append('a')
            i += 1
        else:
            res_val.append(str(b[j]))
            res_str.append('b')
            j += 1
            
    while j < m:
        res_val.append(str(b[j]))
        res_str.append('b')
        j += 1
    while i < n:
        res_val.append(str(a[i]))
        res_str.append('a')
        i += 1   
        

    print(" ".join(res_val))
    print("".join(res_str))

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
solve(n, m, a, b)
