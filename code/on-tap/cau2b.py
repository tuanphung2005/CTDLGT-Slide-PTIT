def solve(n, a):
    total_num = []
    
    for i in range(n):
        for j in range(i, n):
            if i == j:
                total_num.append(a[i])
            else:
                total_num.append(max(a[i:j]))
    
    return total_num

print(solve(4, [1, 3, 1, 7]))
        