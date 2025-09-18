def validAnagram(s, t):
    if not len(s) == len(t):
        return False
    
    char = {}
    char2 = {}

    for i in range(len(s)):
        if s[i] in char.keys():
            char[s[i]] += 1
        else:
            char[s[i]] = 1

        if t[i] in char2.keys():
            char2[t[i]] += 1
        else:
            char2[t[i]] = 1

    return char == char2


s = "rat"
t = "car"
print(validAnagram(s, t))