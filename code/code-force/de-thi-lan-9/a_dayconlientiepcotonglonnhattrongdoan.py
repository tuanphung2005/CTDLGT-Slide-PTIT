from collections import deque
def solve(n, u, v, a):
    s = [0] * (n + 1)
    
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    max_sum = -float("inf")
    dq = deque()
    
    for i in range(u, n + 1):
        j = i - u
        
        while dq and s[dq[-1]] >= s[j]:
            dq.pop()
        dq.append(j)
        
        if dq[0] < i - v:
            dq.popleft()
            
        max_sum = max(max_sum, s[i] - s[dq[0]])
        
    return max_sum
n, u, v = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, u, v, a))