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

def groupAnagram(strs):
    if not strs:
        return []
    
    groups = {}

    for word in strs:
        found = False
        for key in groups:
            if validAnagram(word, key):
                groups[key].append(word)
                found = True
                break
        if not found:
            groups[word] = [word]

    return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))