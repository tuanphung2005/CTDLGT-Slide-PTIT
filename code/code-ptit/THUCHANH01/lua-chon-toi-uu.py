def solve(job):

    job.sort(key=lambda x: x[1])
    # print(job)
    
    c = 0
    end = -1
    for a, b in job:
        if a >= end:
            c += 1
            end = b
    return c

# print(solve([(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]))

T = int(input())
for _ in range(T):
    n = int(input())
    job = []
    for _ in range(n):
        a, b = map(int, input().split())
        job.append((a, b))
    print(solve(job))
