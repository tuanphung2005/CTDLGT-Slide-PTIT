def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def find_min_max(arr, n):
    if n == 1:
        return arr[0], arr[0]
    min_val, max_val = find_min_max(arr, n-1)
    last = arr[n-1]
    if last < min_val:
        min_val = last
    if last > max_val:
        max_val = last
    return min_val, max_val

nums = [3, 5, 1, 8, 2]

print("Max:", find_min_max(nums, len(nums))[1])
print("Min:", find_min_max(nums, len(nums))[0])

print(fibonacci(10))