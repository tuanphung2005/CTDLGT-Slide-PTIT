def solve(s):
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        if s[i] == '0':
            s[i] = '1'
            return ''.join(s)
        else:
            s[i] = '0'
        i -= 1
    return '0' * len(s)

# print(solve('111111'))

T = int(input())

for _ in range(T):
    s = str(input())
    print(solve(s))