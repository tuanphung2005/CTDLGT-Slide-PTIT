from collections import deque
def solve(n, u, v, a):
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + a[i]
    ans = -float('inf')
    
    dq = deque()
    
    for j in range(u, n + 1):
        i = j - u
        while dq and p[dq[-1]] >= p[i]:
            dq.pop()
        dq.append(i)
        
        if dq[0] < j - v:
            dq.popleft()
        ans = max(ans, p[j] - p[dq[0]])
    return ans