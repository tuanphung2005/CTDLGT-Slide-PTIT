def solve(s):
    stack = []
    for i in s:
        if i == "{" or i == "(" or i == "[":
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if i == "}" and top != "{":
                return False
            if i == ")" and top != "(":
                return False
            if i == "]" and top != "[":
                return False
    return len(stack) == 0


print(solve('()'))
print(solve('()[]{}'))
print(solve('(]'))
print(solve("([])"))
