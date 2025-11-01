def solution (arr, N, M):
    max_sum = -10**9 
    min_sum = 10**9
    for i in range (N -M + 1):
        sum = 0
        for j in range (i, i + M):
            sum += arr[j]
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
    return max_sum - min_sum