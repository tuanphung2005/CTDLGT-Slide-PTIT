

def solve(s):
    stack = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if (char == '}' and top != '{') or (char == ']' and top != '[') or (char == ')' and top != '('):
                return False
    return len(stack) == 0

print(solve('{[()]}'))
print(solve('())[(])}'))