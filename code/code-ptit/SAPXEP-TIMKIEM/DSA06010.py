T = int(input())

for _ in range(T):
    n = int(input())
    A = input().replace(" ", "")
    A = sorted(set(A))
    print(*A)