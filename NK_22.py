# def main():
#     n_L = input().strip().split(" ")
#     n = int(n_L[0])
#     L = int(n_L[1])
#
#     store_index = {}
#
#     for i in range(n):
#         xi_yi = input().strip().split(" ")
#         xi = int(xi_yi[0])
#         yi = int(xi_yi[1])
#         if xi not in store_index:
#             store_index[xi] = yi
#         else:
#             store_index[xi] = max(store_index[xi], yi)
#
#     c = 0
#     index = 0
#     xi_list = sorted(list(store_index.keys()),key=lambda x:store_index[x])
#     print(store_index)
#     print(xi_list)
#
#     target_left = 0
#     res = 0
#     for index in range(0, n):
#         if index <= target_left:
#             if index not in store_index:
#                 continue
#             else:
#                 if store_index[index] > target_left:
#                     target_left = store_index[index]
#                     res += 1
#                     if target_left >= L:
#                         print(res)
#                         return
#                 else:
#                     pass
#
#         else:
#             if index not in store_index:
#                 print(-1)
#             else:
#                 res += 1
#                 target_left = store_index[index]
#                 if target_left >= L:
#                     print(res)
#                     return
#
#     if target_left >= L:
#         print(res)
#     else:
#         print(-1)
#
# main()

def main():
    n_L = input().strip().split(" ")
    n = int(n_L[0])
    L = int(n_L[1])

    total_list = []

    for i in range(n):
        xi_yi = input().strip().split(" ")
        xi = int(xi_yi[0])
        yi = int(xi_yi[1])
        total_list.append([xi, yi])

    res = []
    for i in sorted(total_list, key=lambda x: x[0]):
        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(i[1], res[-1][1])
        else:
            res.append(i)
    if len(res) != 1:
        print(-1)
        return
    xx = res[0]
    if res[0][0] > 0:
        print(-1)
        return
    if res[0][-1] < L:
        print(-1)
        return
    print(-1)
main()