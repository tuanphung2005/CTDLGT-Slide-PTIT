#BACKTRACK
def backtrack(start, li):
    if len(li) == k:
        print(" ".join(li))
        return
    for i in range(start, len(res)):
        li.append(res[i])
        backtrack(i + 1, li)
        li.pop()

n, k = map(int, input().split())
names = input().split()

res = sorted(set(names))

backtrack(0, [])