menhgia = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

n = int(input())
for _ in range(n):
    tien = int(input())
    count = 0
    for i in menhgia:
        if tien >= i:
            cnt = tien // i
            # print(cnt)
            count += cnt
            tien -= cnt * i
    print(count)