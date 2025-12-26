def solve(s):
    
    res = []
    
    stack = []
    
    counter = 0
    for i in s:
        
        if i == "(":
            counter += 1
            stack.append(counter)
            res.append(counter)
        elif i == ")":
            val = stack.pop()
            res.append(val)
    res.append('')
    return res
t = int(input())
for _ in range(t):
    s = input()
    print(*solve(s))