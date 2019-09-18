def func(a_list, n):
    if n <= 4:
        return a_list[n-1]
    # else:
    #     return func(a_list, n-1) + func(a_list, n-3) + func(a_list, n-4)
    num4 = a_list[0]
    num3 = a_list[1]
    num2 = a_list[2]
    num1 = a_list[3]
    res = 0
    for i in range(4, n):
        res = num4 + num3 + num1
        num4 = num3
        num3 = num2
        num2 = num1
        num1 = res

    return res



input_string_list = input().strip().split(" ")

input_int_list = list(map(int, input_string_list))

a_list = input_int_list[:4]

n = input_int_list[4]
res = func(a_list, n) % (10**9+7)
print(res)




