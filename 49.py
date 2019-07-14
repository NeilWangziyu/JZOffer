# https://leetcode-cn.com/problems/ugly-number-ii/submissions/
# 空间换时间
def GetUglyNUmber(index):
    if index <= 0:
        return 0
    Ugly_list = [-1 for _ in range(index)]
    Ugly_list[0] = 1
    nextUgly_index  = 1


    multiply_two = 0
    multiply_three = 0
    multiply_five = 0
    while(nextUgly_index < len(Ugly_list)):
        min_number = min(Ugly_list[multiply_two] * 2, Ugly_list[multiply_three] * 3, Ugly_list[multiply_five] * 5)
        Ugly_list[nextUgly_index] = min_number
        while(Ugly_list[multiply_two] * 2 <= Ugly_list[nextUgly_index]):
            multiply_two += 1
        while (Ugly_list[multiply_three] * 3 <= Ugly_list[nextUgly_index]):
            multiply_three += 1
        while (Ugly_list[multiply_five] * 5 <= Ugly_list[nextUgly_index]):
            multiply_five += 1

        nextUgly_index += 1
    return Ugly_list[-1]


print(GetUglyNUmber(150))