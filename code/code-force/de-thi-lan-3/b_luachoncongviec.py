import heapq

def solve(n, a):
    a.sort()

    min_heap = []
    for s, p in a:
        heapq.heappush(min_heap, p)

        if len(min_heap) > s:
            heapq.heappop(min_heap)

    return sum(min_heap)

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(solve(n, a))