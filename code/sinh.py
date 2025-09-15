def nhi_phan(n):
    a = [0] * n
    while True:
        print("".join(map(str, a)))
        i = n - 1
        while i >= 0 and a[i] == 1:
            i -= 1
        if i < 0:
            break
        a[i] = 1
        for j in range(i+1, n):
            a[j] = 0

def to_hop(n, k):
    a = list(range(1, k+1))
    while True:
        print(*a)
        i = k - 1
        while i >= 0 and a[i] == n - k + i + 1:
            i -= 1
        if i < 0:
            break
        a[i] += 1
        for j in range(i+1, k):
            a[j] = a[j-1] + 1

def hoan_vi(n):
    a = list(range(1, n+1))
    while True:
        print(*a)
        i = n - 2
        while i >= 0 and a[i] > a[i+1]:
            i -= 1
        if i < 0:
            break
        j = n - 1
        while a[j] < a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
        
        left, right = i+1, n-1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1



n = 5
k = 3

print("a) Xâu nhị phân độ dài n=5:")
nhi_phan(n)

print("b) Tổ hợp chập k=3 của n=5:")
to_hop(n, k)

print("c) Hoán vị của n=5:")
hoan_vi(n)
