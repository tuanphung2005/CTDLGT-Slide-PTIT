def check(expr):
    stack = []
    for i in range(len(expr)):
        if expr[i] == ')':
            top = stack.pop()
            flag = True
            while top != '(':
                if top in '+-*/':
                    flag = False
                top = stack.pop()
            if flag:
                return True
        else:
            stack.append(expr[i])
    return False

n = int(input())
for _ in range(n):
    exp = input().strip()
    if check(exp):
        print("Yes")
    else:
        print("No")