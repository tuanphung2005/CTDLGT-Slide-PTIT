def isnext(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def sinh(pos, used, current, result, m, n):
    if len(current) > 0:
        valid = True
        for i in range(1, len(current)):
            x1, y1 = current[i-1]
            x2, y2 = current[i]
            if not isnext(x1, y1, x2, y2):
                valid = False
                break
        if valid:
            result.append(current[:])

    if len(current) == m * n:
        return

    for i in range(len(pos)):
        if not used[i]:
            used[i] = True
            current.append(pos[i])
            sinh(pos, used, current, result, m, n)
            current.pop()
            used[i] = False


def solve(board, m, n):
    positions = []
    for i in range(m):
        for j in range(n):
            positions.append((i, j))

    used = [False] * len(positions)
    path = []
    sinh(positions, used, [], path, m, n)

    words = []
    for path in path:
        word = ""
        for (x, y) in path:
            word += board[x][y]
        words.append(word)
    return words


T = int(input())
for _ in range(T):
    line = input().strip()
    while line == "":
        line = input().strip()
    k, m, n = map(int, line.split())

    dic = input().strip().split()

    board = []
    for i in range(m):
        row = input().strip().split()
        board.append(row)

    res = solve(board, m, n)

    found = []
    for i in dic:
        if i in res:
            found.append(i)

    if len(found) == 0:
        print(-1)
    else:
        found.sort()
        print(" ".join(found))
