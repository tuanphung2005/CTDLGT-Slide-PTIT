from itertools import combinations_with_replacement

chars = "ABCDEFGHIJK"

# for i in chars:
#     print(i)
# 
c, K = input().split()

K = int(K)

temp = []

# print(c, K)
for i in chars:
    temp.append(i)
    if i == c:
        break
# print(temp)

comb = list(combinations_with_replacement(temp, K))
for i in comb:
    print("".join(i))