def solve(A):
    max_list = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            max_list.append(max(A[i:j + 1]))
    
    
    return max_list

T = 1
n = 4
A = [1, 3, 1, 7]

print(solve(A))
# print(A[0:3])
# print(max(A[0:3]))
