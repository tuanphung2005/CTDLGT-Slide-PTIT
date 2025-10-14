def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        L = min(arr)
        R = max(arr)
        arr.sort()
        have = 1
        for i in range(1, n):
            if arr[i] != arr[i-1]:
                have += 1
        print((R - L + 1) - have)

solve()