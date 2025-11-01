def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(pairs):
    max = 0
    for a, b in pairs:
        g = gcd(a, b)
        if g > max:
            max = g
    return max