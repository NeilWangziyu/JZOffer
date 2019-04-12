def main():
    N = int(input().strip())
    list_p = []
    for i in range(N):
        p_n = float(input().strip())
        list_p.append(p_n)
    res = 0
    len_list = len(list_p)
    mult = 100 // len_list + 1
    final_list = list_p * mult
    total_value = 1
    for index, each in enumerate(final_list):
        if index > 10:
            break
        if index % 2 == 0:
            res += total_value * each
            total_value *= (1-each)

        else:
            total_value *= (1-each)

    print("%.4f" % res)
main()
