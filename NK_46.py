def fun(k):
    # 所有里面回文数
    weishu = 1
    num = 9
    ans = 0
    while (k - num > 0):
        k -= num
        if (weishu % 2 == 0):
            num *= 10

        weishu += 1
    half_ken = (weishu + 1) // 2
    left = 1
    i = 2
    while (i <= half_ken):
        left *= 10
        i += 1

    left += (k - 1)
    ans += left
    if (weishu % 2 != 0):
        left //= 10
    while (left):
        # print(ans, left)
        ans = ans * 10 + left % 10
        left = left // 10

    return ans

num_list = [0, 9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000, 900000, 900000, 9000000, 9000000, 90000000, 90000000,900000000, 900000000,9000000000, 9000000000]

n = int(input().strip())
res = []
for i in range(n):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    if n == 1:
        print(m-1)
    else:
        print(fun(sum(num_list[:n]) + m))
