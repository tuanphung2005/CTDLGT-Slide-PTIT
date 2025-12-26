def solve(n, a):
    stack = []
    
    toantu = "+-*/"
    
    if a[0] in toantu:
        for i in range(len(a) - 1, -1, -1):
            if a[i] not in toantu:
                stack.append(a[i])
            else:
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                if a[i] == "+":
                    temp = o1 + o2
                elif a[i] == "-":
                    temp = o1 - o2
                elif a[i] == "*":
                    temp = o1 * o2
                elif a[i] == "/":
                    temp = o1 / o2
                stack.append(int(temp))
    else:
        for i in range(len(a)):
            if a[i] not in toantu:
                stack.append(a[i])
            else:
                o2 = int(stack.pop())
                o1 = int(stack.pop())
    
                if a[i] == "+":
                    temp = o1 + o2
                elif a[i] == "-":
                    temp = o1 - o2
                elif a[i] == "*":
                    temp = o1 * o2
                elif a[i] == "/":
                    temp = o1 / o2
                    
                stack.append(int(temp))
    
    return stack[0]
# n = 7
# a = ["2", "3", "1", "*", "+", "9", "-"]

T = int(input())
for _ in range(T):
    n = int(input())
    a = input().split()
    print(solve(n, a))