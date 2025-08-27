T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    
    sum = 0
    ans = float('inf')

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = A[i] + A[j]
            if abs(sum) < abs(ans):
                ans = sum
    print(ans)
