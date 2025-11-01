def solve(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    max_freq = -1
    best = -1
    for k, v in freq.items():
        if v > max_freq or (v == max_freq and k < best):
            max_freq = v
            best = k
    return best