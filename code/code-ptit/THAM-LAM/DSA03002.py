def pos(c, s):
    res = []
    for i in range(len(s)):
        if c == s[i]:
            res.append(i)
    return res

def solve(a, b):
    a = list(a)
    b = list(b)
    
    min_sum = 0
    max_sum = 0
    
    pos_a_6 = pos("6", a)
    pos_b_6 = pos("6", b)
    for i in pos_a_6:
        a[i] = "5"
    for i in pos_b_6:
        b [i] = "5"
    min_sum = int(''.join(a)) + int(''.join(b))
    
    pos_a_5 = pos("5", a)
    pos_b_5 = pos("5", b)
    for i in pos_a_5:
        a[i] = "6"
    for i in pos_b_5:
        b [i] = "6"
    max_sum = int(''.join(a)) + int(''.join(b))
    
    return min_sum, max_sum

# print(pos('5', '4852'))
# print(solve('11', '25'))
# print(solve('11', "25"))
a, b = map(str, input().split())
print(*solve(a, b))