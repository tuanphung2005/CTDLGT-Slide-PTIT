def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        dict_arr = {}
        for x in arr:
            dict_arr[x] = dict_arr.get(x, 0) + 1
        # for x in arr:
        #     if x in dict_arr:
        #         dict_arr[x] += 1
        #     else:
        #         dict_arr[x] = 1
        key_arr = []
        key_arr = sorted(dict_arr.keys(), key=lambda x: (-dict_arr[x], x))
        for x in key_arr:
            print((str(x) + ' ') * dict_arr[x], end='')
        # for x in arr:
        #     if x not in key_arr:
        #         key_arr.append(x)
        # # print(len(key_arr))
        # for i in range(len(key_arr)):
        #     for j in range(0, len(key_arr)-i-1):
        #         if dict_arr[key_arr[j]] < dict_arr[key_arr[j+1]]:
        #             key_arr[j], key_arr[j+1] = key_arr[j+1], key_arr[j]
        #         elif dict_arr[key_arr[j]] == dict_arr[key_arr[j+1]] and key_arr[j] > key_arr[j+1]:
        #             key_arr[j], key_arr[j+1] = key_arr[j+1], key_arr[j]

        # for x in key_arr:
        #     for _ in range(dict_arr[x]):
        #         print(x, end=' ')
        print()

solve()