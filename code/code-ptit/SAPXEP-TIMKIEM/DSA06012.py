T = int(input())

for _ in range(T):
    N, k = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    print(*A[-k:][::-1])