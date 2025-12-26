def solve(s):
    # 
    dp = [0] * 26

    for char in s:
        # val tu char - A
        val = ord(char) - ord('A')
        current_max = 0

        # kiem tra tu 0 den val
        for i in range(val + 1):
            current_max = max(current_max, dp[i])
        dp[val] = current_max + 1

    return max(dp)

s = input()
print(solve(s))