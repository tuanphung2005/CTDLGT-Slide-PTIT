def solve(n, a):
    
    stack = []
    
    toantu = "+-*/"
    
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
                
    
    return (stack[0])
    
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(input().split())
    print(solve(n, a))