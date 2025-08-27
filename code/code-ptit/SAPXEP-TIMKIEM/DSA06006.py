T = int(input())

def sort012(arr):
    # c0 = 0
    c1 = 0
    c2 = 0

    sorted_arr = []

    for i in range(len(arr)):
        if arr[i] == 0:
            sorted_arr.append(0)
        elif arr[i] == 1:
            c1 += 1
        else:
            c2 += 1

    sorted_arr.extend([1] * c1)
    sorted_arr.extend([2] * c2)

    return sorted_arr

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    A = sort012(A)
    print(*A)
