def main():
    # 线段树
    # 50%
    n = int(input().strip())
    each_list = input().strip().split()
    each_list = list(map(int, each_list))

    sum_list = [0]
    s = 0
    for each in each_list:
        s += each
        sum_list.append(s)
    max_sum = 0

    for i in range(n):
        tem_min = each_list[i]
        for j in range(i+1, n+1):
            tem_min = min(tem_min, each_list[j-1])
            max_sum = max(max_sum, (sum_list[j]-sum_list[i]) * tem_min)
    print(max_sum)
main()

# 5
# 7 2 4 6 5