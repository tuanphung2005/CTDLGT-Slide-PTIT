def check(day, month, year):
    if month < 1 or month > 12:
        return False
    days = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days[month - 1]:
        return False
    return True


res = []

for a in "02":
    for b in "02":
        for c in "02":
            for d in "02":
                # half = a + b + c + d
                # full = half + half[::-1]
                full = a + b + c + d + d + c + b + a

                dd = int(full[0:2])
                mm = int(full[2:4])
                yyyy = int(full[4:8])

                if yyyy >= 2000 and check(dd, mm, yyyy):
                    res.append(f"{full[0:2]}/{full[2:4]}/{full[4:8]}")

res.sort()

for r in res:
    print(r)
