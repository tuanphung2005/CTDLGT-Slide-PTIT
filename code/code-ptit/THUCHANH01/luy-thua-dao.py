MOD = 10**9 + 7
PHI = MOD - 1

def mod_from_str(s, mod):
    res = 0
    for ch in s:
        res = (res * 10 + (ord(ch) - 48)) % mod
    return res

T = int(input().strip())
for _ in range(T):
    sN = input().strip()

    base_mod = mod_from_str(sN, MOD)

    R_str = sN[::-1]

    R_str = R_str.lstrip('0')
    if R_str == '':
        R_str = '0'

    if base_mod == 0:
        print(0)
        continue

    exp_mod = mod_from_str(R_str, PHI)

    print(pow(base_mod, exp_mod, MOD))
