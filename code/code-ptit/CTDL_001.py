n = int(input())
def is_palindrome(s):
    return s == s[::-1]

def gen(n):
    if n < 0:
        return []
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]
    b_thuannghich = gen(n - 2)
    thuannghich = []
    for s in b_thuannghich:
        thuannghich.append("0" + s + "0")
        thuannghich.append("1" + s + "1")
    return thuannghich

p = gen(n)
p.sort()
for s in p:
    print(s)