def solve(matrix):
    count = 0
    for col in range(n):
        max = matrix[0][col]
        for row in range(1, n):
            if matrix[row][col] > max:
                max = matrix[row][col]
        # print(max)
        count += max
    print(count)

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    solve(matrix)