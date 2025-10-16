def solve(n, k):
    s = [''] * n
    result = []

    def backtrack(i, count):
        if i == n:
            if count == k:
                result.append(''.join(s))
            return

        s[i] = '0'
        backtrack(i + 1, count)

        if count < k:
            s[i] = '1'
            backtrack(i + 1, count + 1)

    backtrack(0, 0)
    return result


# driver
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    for x in solve(n, k):
        print(x)
