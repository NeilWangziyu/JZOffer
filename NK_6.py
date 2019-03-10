# chaoshi-------
# def main():
#     n, d = input().strip().split()
#     n = int(n)
#     d = int(d)
#     dict_bank = {}
#     min_index = float('inf')
#     max_index = -float('inf')
#     for i in range(n-1):
#         index, value = input().strip().split()
#         index = int(index)
#         value = int(value)
#         dict_bank[index] = value
#         if index < min_index:
#             min_index = index
#         if index > max_index:
#             max_index = index
#     max_money = 0
#     for each_bank in (dict_bank.keys()):
#         total_money = dict_bank[each_bank]
#         money = dict_bank[each_bank]
#         dis_range_a = each_bank - d
#         dis_range_b = each_bank + d
#         if dis_range_a >= min_index:
#             for i in range(min_index, dis_range_a+1):
#                 if i in dict_bank:
#                     if dict_bank[i] + money > total_money:
#                         total_money = dict_bank[i] + money
#
#         if dis_range_b <= max_index:
#             for i in range(dis_range_b, max_index+1):
#                 if i in dict_bank:
#                     if dict_bank[i] + money > total_money:
#                         total_money = dict_bank[i] + money
#         if max_money < total_money:
#             max_money = total_money
#     print(max_money)
# main()





# chaoshi-------
# def main():
#     n_d = input().strip().split(' ')
#     n = int(n_d[0])
#     d = int(n_d[1])
#     pos = []
#     for i in range(n):
#         line = input().strip().split(' ')
#
#         pos.append([int(line[0]),int(line[1])])
#     max_sum = 0
#     for i in range(n):
#         left = pos[i:]
#         left_after_sort = sorted(left, key=lambda x:x[1], reverse=True)
#         for each in left_after_sort:
#             if abs(pos[i][0] - each[0])>=d:
#                 print(each)
#                 max_sum = max(max_sum, pos[i][1]+each[1])
#                 break
#     print(max_sum)
# main()

str="""
23 3
1 1
3 5
4 8
6 4
10 3
11 2
15 7
20 9
21 10
22 11
25 1
29 7
100 8
1002 15
1003 15
1004 15
1005 15
1006 15
1007 15
1008 15
1018 15
1108 16
1109 17

"""

# n_d = input().strip().split(' ')
# n = int(n_d[0])
# d = int(n_d[1])
# pos = []
# money = []
# for i in range(n):
#     line = input().strip().split(' ')
#     pos.append(int(line[0]))
#     money.append(int(line[1]))
# max_sum = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if abs(pos[j]-pos[i])>=d:
#             max_sum = max(max_sum, money[i]+money[j])
# print(max_sum)






# wrong-------
# def main():
#     n_d = input().strip().split(' ')
#     n = int(n_d[0])
#     d = int(n_d[1])
#     pos = []
#     money = []
#     for i in range(n):
#         line = input().strip().split(' ')
#         pos.append(int(line[0]))
#         money.append(int(line[1]))
#
#     max_sum = 0
#     init_i = 0
#     init_j = len(pos)-1
#     while(abs(pos[init_j] - pos[init_i]) >= d):
#         print(init_i, init_j)
#         max_sum = max(max_sum, money[init_j] + money[init_i])
#         if money[init_i+1] - money[init_i] > money[init_j-1]-money[init_j]:
#             init_i += 1
#         else:
#             init_j -= 1
#     print(max_sum)
#
# main()




# -----------
# wrong
# from operator import itemgetter
#
# n_d = input().strip().split(' ')
# n = int(n_d[0])
# d = int(n_d[1])
#
# dots = []
# max_x = 0
# for i in range(n):
#     line = input().strip().split(' ')
#     x = int(line[0])
#     value = int(line[1])
#     dots.append((int(x), int(value)))
#     if int(x) > max_x:
#         max_x = int(x)
#
# dots = sorted(dots, key=itemgetter(0))
# dots_map = {x: value for x, value in dots}
#
# x_s = [dot[0] for dot in dots if dot[0] + d <= max_x]
#
# global_max = 0
#
# sliding_window_start = x_s[0]
#
# left = [dot for dot in dots if dot[0] <= sliding_window_start ]
# right = [dot for dot in dots if dot[0] > sliding_window_start + d]
# right_value_sorted = sorted(right, key=itemgetter(1), reverse=True)  # 从大到小
#
# left_max = sorted(left, key=itemgetter(1))[-1]
# right_max = right_value_sorted[0]
# global_max = left_max[1] + right_max[1]
#
# for sliding_window_start in x_s:
#     left_pushed = dots_map[sliding_window_start]
#     if left_max[1] < left_pushed[1]:
#         left_max = left_pushed
#     right_poped = right[0]
#     if right_max[1] == right_poped[1]:  # 最大者被弹出
#         right_value_sorted = right_value_sorted[:1]
#         right_max = right_value_sorted[0]
#     if global_max < left_max[1] + right_max[1]:
#         global_max = left_max[1] + right_max[1]
#
#     left.append(left_pushed)
#     right.pop(0)
#
# print(global_max)


# ------超时
# def main():
#     n_d = input().strip().split(' ')
#     n = int(n_d[0])
#     d = int(n_d[1])
#     pos = []
#     for i in range(n):
#         line = input().strip().split(' ')
#
#         pos.append([int(line[0]),int(line[1])])
#     max_sum = 0
#     after_sort = sorted(pos, key=lambda x:x[1], reverse=True)
#     for i in range(len(after_sort)):
#         for j in range(i, len(after_sort)):
#             if abs(after_sort[i][0] - after_sort[j][0])>=d:
#                 max_sum = max(max_sum, after_sort[i][1]+after_sort[j][1])
#     print(max_sum)
# main()

# ------错时35%
# from operator import itemgetter
#
# n, d = input().strip().split()
# n = int(n)
# d = int(d)
# dots = []
# max_x = 0
# for _ in range(n):
#     x, value = input().strip().split()
#     dots.append((int(x), int(value)))
#     if int(x) > max_x:
#         max_x = int(x)
# dots = sorted(dots, key=itemgetter(0))
# dots_map = {x: (x, value) for x, value in dots}
#
# x_s = [dot[0] for dot in dots if dot[0] + d <= max_x]
# global_max = 0
# sliding_window_start = x_s[0]
# left = [dot for dot in dots if dot[0] <= sliding_window_start]
# right = [dot for dot in dots if dot[0] >= sliding_window_start + d]
# right_value_sorted = sorted(right, key=itemgetter(1), reverse=True)  # 从大到小
#
# left_max = sorted(left, key=itemgetter(1))[-1]
# right_max = right_value_sorted[0]
# global_max = (left_max, right_max)
#
# for sliding_window_start in x_s[1:]:
#     left_pushed = dots_map[sliding_window_start]
#     left.append(left_pushed)
#     if left_max[1] < left_pushed[1]:
#         left_max = left_pushed
#
#     right_poped = []
#     while right[0][0] < sliding_window_start + d:
#         right_poped.append(right.pop(0))
#
#     if right_max[0] in [dot[0] for dot in right_poped]:  # 最大者被弹出
#         right_value_sorted = right_value_sorted[len(right_poped):]
#         right_max = right_value_sorted[0]
#
#     if global_max[0][1] + global_max[1][1] < left_max[1] + right_max[1]:
#         global_max = (left_max, right_max)
#
#
# print(global_max[0][1] + global_max[1][1])