def funct(n, m):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    else:
        if m - 1 == 0:
            return n / (n + m)
        if m - 2 == 0:
            return n / (n + m) + m / (n + m) * (m - 1) / (n + m - 1)
        else:
            next_A_per1 = funct(n - 1, m - 2)
            next_A_per2 = funct(n, m - 3)
            return n / (n + m) + (m / (n + m))* ((m - 1) / (n + m - 1)) * n/(n + m - 2) * next_A_per1 + (m / (n + m))*((m-1) / (n + m - 1)) * (m-2) /(n + m - 2) * next_A_per2

input_list = input().strip().split(" ")
n = int(input_list[0])
m = int(input_list[1])
if n == 0:
    print(0.00000)
A_percentage = funct(n, m)
print('%.5f' % A_percentage)


