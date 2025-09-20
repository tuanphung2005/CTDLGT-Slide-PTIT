# TODO: i dont understand this shit
def topKFrequentElements(nums, k):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    #for k, v in freq.items():
        #print(k, v)
    max_freq = len(nums)
    buckets = [[] for _ in range(max_freq + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    res = []
    for i in range(max_freq, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res
    return res

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

print(topKFrequentElements(nums, k))