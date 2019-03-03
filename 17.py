def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return ""
    elif n == 1:
        return ['1']
    else:
        num_list = [0] * n
        Print1ToMaxOfNDigits_core(num_list, n, 0)


def Print1ToMaxOfNDigits_core(num_list, n, index):
    if index == n:
        print_list_num(num_list)
    else:
        Print1ToMaxOfNDigits_core(num_list, n, index + 1)
        for i in range(0, 9):
            num_list[index] += 1
            if num_list[index] == 10:
                num_list[index] = 0
            Print1ToMaxOfNDigits_core(num_list, n, index+1)

def print_list_num(num_list):
    init = 0
    while(init < len(num_list) and num_list[init]==0):
        init += 1
    if init == len(num_list):
        return
    else:
        print(num_list[init:])




if __name__ == "__main__":
    print(Print1ToMaxOfNDigits(3))