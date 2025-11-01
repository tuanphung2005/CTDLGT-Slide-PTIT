def solve(matrix):
    avg = []

    for i in range(5):
        s = 0
        for j in range(5):
            s += matrix[i][j]
        avg.append(s // 5)

    for j in range(5):
        s = 0
        for i in range(5):
            s += matrix[i][j]
        avg.append(s // 5)

    s = 0
    for i in range(5):
        s += matrix[i][i]
    avg.append(s // 5)

    s = 0
    for i in range(5):
        s += matrix[i][4 - i]
    avg.append(s // 5)

    return max(avg) + min(avg)