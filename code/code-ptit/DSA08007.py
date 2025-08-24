# TODO: TLE
def countbdn(n):
    def dfs(current):
        if current > n:
            return 0
        
        count = 1
        next_0 = current * 10
        next_1 = current * 10 + 1
        
        if next_0 <= n:
            count += dfs(next_0)
        if next_1 <= n:
            count += dfs(next_1)
            
        return count
    
    if n < 1:
        return 0
    
    return dfs(1)

t = int(input())
    
for _ in range(t):
    n = int(input())
    result = countbdn(n)
    print(result)