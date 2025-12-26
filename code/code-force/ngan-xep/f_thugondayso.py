def solve(n, a):
    # chan + chan, le + le
    stack = []
    for i in a:
        if not stack:
            stack.append(i)
        else:
            if (stack[-1] + i) % 2 == 0:
                stack.pop()
            else:
                stack.append(i)
    return len(stack)
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))