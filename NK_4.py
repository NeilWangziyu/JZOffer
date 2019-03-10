import sys


def main():
    n = int(input().strip())
    a_string = list(input().strip().split())
    b_string = list(input().strip().split())

    a_list = sorted((map(int, a_string)), reverse=False)
    b_list = sorted((map(int, b_string)), reverse=True)
    s = 0
    for i in range(len(a_list)):
        s += a_list[i] * b_list[i]
    print(s)


main()