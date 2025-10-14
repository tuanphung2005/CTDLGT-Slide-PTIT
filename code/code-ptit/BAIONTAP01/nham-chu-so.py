# def solve(A, B):
#     s1 = A + B

#     A = str(A)
#     B = str(B)
#     # for i in range(len(A)):
#     #     if A[i] == '5':
#     #         A = A[:i] + '6' + A[i+1:]
#     #     elif A[i] == '6':
#     #         A = A[:i] + '5' + A[i+1:]
#     # for i in range(len(B)):
#     #     if B[i] == '5':
#     #         B = B[:i] + '6' + B[i+1:]
#     #     elif B[i] == '6':
#     #         B = B[:i] + '5' + B[i+1:]
#     for i in range(len(A)):
#         for j in range(len(B)):
#     s2 = int(A) + int(B)
#     return s2, s1

# a, b = map(int, input().split())
# print(*(sorted(solve(a, b))))
    
# print(solve(11, 25))

def solve(A, B):
    A = str(A)
    B = str(B)

    for i in range(len(A)):
        if A[i] == '6':
            A = A[:i] + '5' + A[i+1:]
    for i in range(len(B)):
        if B[i] == '6':
            B = B[:i] + '5' + B[i+1:]
    min_sum = int(A) + int(B)
    for i in range(len(A)):
        if A[i] == '5':
            A = A[:i] + '6' + A[i+1:]
    for i in range(len(B)):
        if B[i] == '5':
            B = B[:i] + '6' + B[i+1:]
    max_sum = int(A) + int(B)

    return min_sum, max_sum

a, b = map(int, input().split())
min, max = solve(a, b)
print(min, max)