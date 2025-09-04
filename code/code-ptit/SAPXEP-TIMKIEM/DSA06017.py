def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    merged = a + b
    merged.sort()
    print(*merged)

T = int(input())
for _ in range(T):
    solve()