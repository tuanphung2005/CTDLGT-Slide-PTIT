
def solve(n, s, a):
    
    def backtrack(i, temp):
        if i == n:
            return 1 if temp == s else 0
        
        include = backtrack(i + 1, temp + a[i])
        exclude = backtrack(i + 1, temp)
        
        return include + exclude
    
    res = backtrack(0, 0)
    
    if s == 0:
        res -= 1
        
    print(res)
    
    return
    
n, s = map(int, input().split())
a = list(map(int, input().split()))
solve(n, s, a)