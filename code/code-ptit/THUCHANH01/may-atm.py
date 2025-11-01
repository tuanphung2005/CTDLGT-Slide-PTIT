def backtrack(t, s, i, cur_sum, cur_cnt, ans):
    if cur_sum == s:
        ans[0] = min(ans[0], cur_cnt)
        return
    if i == len(t) or cur_sum > s or cur_cnt >= ans[0]:
        return
    
    backtrack(t, s, i + 1, cur_sum, cur_cnt, ans)
    backtrack(t, s, i + 1, cur_sum + t[i], cur_cnt + 1, ans)


def solve(t, s):
    ans = [float('inf')]
    backtrack(t, s, 0, 0, 0, ans)
    if ans[0] == float('inf'):
        return -1
    else:
        return ans[0]

T = int(input())
for _ in range(T):
    n, s = map(int, input().split())
    t = list(map(int, input().split()))
    print(solve(t, s))