def solve(s):
    s = list(s)
    n = len(s)

    i = n - 1
    while i >= 0 and s[i] == "0":
        s[i] = "1"
        i -= 1
    
    if i >= 0:
        s[i] = "0"
    else:
        s = "1" * n

    return ''.join(s)

T = int(input())
for _ in range(T):
    s = str(input())
    print(solve(s))
