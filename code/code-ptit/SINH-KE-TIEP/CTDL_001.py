def solve(n, s="", pos=0):
    if pos == n // 2:
        if n % 2 == 1:
            full = s + '0' + s[::-1]
            print(' '.join(full))
            full = s + '1' + s[::-1]
            print(' '.join(full))
        else:
            full = s + s[::-1]
            print(' '.join(full))
        return

    solve(n, s + '0', pos + 1)
    solve(n, s + '1', pos + 1)

n = int(input())
solve(n)