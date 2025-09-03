def test():
    n, m = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    max1 = max(a1)
    min2 = min(a2)
    return max1 * min2

T = int(input())
for _ in range(T):
    print(test())