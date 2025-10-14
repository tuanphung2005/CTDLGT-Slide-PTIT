def insertion_sort(arr, n):
    for i in range(n):
        tmp = arr[:i+1]
        for j in range(1, len(tmp)):
            key = tmp[j]
            k = j - 1
            while k >= 0 and key < tmp[k]:
                tmp[k + 1] = tmp[k]
                k -= 1
            tmp[k + 1] = key
        print(f"Buoc {i}: {' '.join(map(str, tmp))}")

n = int(input())
a = list(map(int, input().split()))
insertion_sort(a, n)