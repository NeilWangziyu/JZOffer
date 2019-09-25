# from collections import Counter
# # n = int(input().strip())
# # input_list = input().strip().split()
# # M = int(input().strip())
# #
# # for i in range(M):
# #     l_str,r_str = input().strip().split()
# #     l = int(l_str)
# #     r = int(r_str)
# #     c = Counter(input_list[l-1:r])
# #     res = 0
# #     for each in c.keys():
# #         if c[each] == 1:
# #             res += 1
# #     print(res)
# #

from collections import Counter
n = int(input().strip())
input_list = input().strip().split()
M = int(input().strip())

dp = [{}]
dict_tem = {}
for each in input_list:
    if each not in dict_tem:
        dict_tem[each] = 1
    else:
        dict_tem[each] += 1
    dp.append(dict_tem.copy())

# print(dp)
for i in range(M):
    l_str,r_str = input().strip().split()
    l = int(l_str)
    r = int(r_str)
    base_dict = dp[r].copy()
    # print(base_dict)
    for each in dp[l-1].keys():
        base_dict[each] -= dp[l-1][each]

    res = 0
    # print(base_dict)
    for each in base_dict.keys():
        if base_dict[each] == 1:
            res += 1
    print(res)