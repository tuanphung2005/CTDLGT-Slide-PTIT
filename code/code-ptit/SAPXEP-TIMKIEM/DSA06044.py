n = int(input())
arr = list(map(int, input().split()))

a = []
b = []
for i in range(n):
    if (i + 1) % 2 == 1:
        a.append(arr[i])
    else:
        b.append(arr[i])

a.sort()
b.sort(reverse=True)

result = []
for i in range(len(b)):
    result.append(a[i])
    result.append(b[i])
if n % 2 == 1:
    result.append(a[-1])

print(*result)