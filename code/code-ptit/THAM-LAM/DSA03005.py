def solve(n, k, a):
    a.sort()

    sum1 = 0
    sum2 = 0
    max_sum = 0

    for i in range(1, n):
        # print(a[0:i], a[i:n])
        if (len(a[0:i]) == (n - k) and len(a[i:n]) == k) or (len(a[i:n]) == (n - k) and len(a[0:i]) == k):
            sum1 = sum(a[0:i])
            sum2 = sum(a[i:n])
            current_sum = abs(sum1 - sum2)
            # print(current_sum)
            max_sum = max(current_sum, max_sum)

    print(max_sum)
    
# a = [8, 4, 5, 2, 10]
# a.sort()
# solve(5, 2, [8, 4, 5, 2, 10])
# solve(8, 3, [1, 1, 1, 1, 1, 1, 1, 1])
# print(a[0:1], a[1:5])
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, k, a)