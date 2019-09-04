def main():
    nm = input().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    a_list = input().strip().split()
    a = list(map(int, a_list))

    b_list = input().strip().split()
    b = list(map(int, b_list))

    a_odd = 0
    a_Even = 0
    for each in a:
        if each % 2 == 0:
            a_Even += 1
        else:
            a_odd += 1

    b_odd = 0
    b_even = 0
    for each in b:
        if each % 2 == 0:
            b_even += 1
        else:
            b_odd += 1
    print(min(a_odd, b_even) + min(a_Even, b_odd))



