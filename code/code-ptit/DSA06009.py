T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    freq = {}
    for num in a:
        count += freq.get(k - num, 0)
        freq[num] = freq.get(num, 0) + 1
    print(count)