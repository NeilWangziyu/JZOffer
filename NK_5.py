def main():
    a_input = input().strip()
    a_list = list(a_input.lower())
    start = a_list[0]
    for i in range(1, len(a_list)-1):
        first_part = a_list[:i]
        second_part = a_list[i:]
        set_f = set(first_part)
        set_s = set(second_part)
        if set_f.issubset(set_s):
            if a_list[i] < start:
                start = a_list[i]
    print(start)

main()



