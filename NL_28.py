def main():
    n = int(input().strip())
    input_N_list_all = []
    N_all = []
    input_M_list_all = []
    for i in range(n):
        input_N_list = list(input().strip())
        input_N_list_all.append(input_N_list)
        N = len(input_N_list)
        N_all.append(N)
        input_M_list = list(input().strip())
        input_M_list_all.append(input_M_list)

    for i in range(n):
        input_N_list = input_N_list_all[i]
        N = N_all[i]
        input_M_list = input_M_list_all[i]

        res = []
        def DFS(input_N_list, input_M_list, N, new_list, res_list):
            if N == 0:
                if new_list == input_M_list:
                    res.append(res_list)
                    return
            if len(new_list) > len(input_M_list):
                return
            if not input_N_list:
                return

            left_card = input_N_list[0]
            DFS(input_N_list[1:], input_M_list,N-1,  new_list, res_list+["d"])
            DFS(input_N_list[1:], input_M_list,N-1,  [left_card]+new_list, res_list+["l"])
            DFS(input_N_list[1:], input_M_list, N-1, new_list+[left_card], res_list+["r"])

        DFS(input_N_list, input_M_list, N, [], [])
        res.sort()

        print("{")
        for each in res:
            print(" ".join(each))
        print("}")
main()

# 3
# 123
# 3
# 123
# 321
# 45
# 67
