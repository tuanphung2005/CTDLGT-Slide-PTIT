def solve(s):
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] != "(":
                return "NO"
            stack.pop()
        elif i == "]":
            if not stack or stack[-1] != "[":
                return "NO"
            stack.pop()
    if stack: return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))