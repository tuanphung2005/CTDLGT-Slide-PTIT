def solve(n):
    
    res = []
    def backtrack(i, open, close):
        
        if len(i) == 2 * n:
            res.append(i)
        
        if open < n:
            backtrack(i + '(', open + 1, close)
        if close < open:
            backtrack(i + ')', open, close + 1)
    
    backtrack("", 0, 0)
    print(len(res))
    for r in res:
        print(r)

solve(int(input()))