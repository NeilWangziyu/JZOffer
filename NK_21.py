def func(input_str):
    if not input_str:
        return input_str
    else:
        total_c = 0
        total_x = 0
        for each in input_str:
            if each == "|":
                total_c += 1
            if each == "[":
                total_x += 1

        if total_c == 0 and total_x == 0:
            return input_str
        elif total_x == 0:
            index_mid = input_str.find("|")
            multiple = int(input_str[:index_mid])
            left = input_str[index_mid + 1:]
            return func(multiple * left)

        elif total_c == 1:
            init = 0
            while(input_str[init] != "["):
                init += 1
            count = 1
            second = init + 1
            while(True):
                if input_str[second] == "]":
                    count -= 1
                    if count == 0:
                        break
                    else:
                        second += 1

                elif input_str[second] == "[":
                    count += 1
                    second += 1
                else:
                    second += 1
            # find init and second
            return input_str[:init] + func(input_str[init+1:second]) + input_str[second + 1:]

        else:
            # only more than one []
            init = 0
            while (input_str[init] != "["):
                init += 1
            count = 1
            second = init + 1
            while (True):
                if input_str[second] == "]":
                    count -= 1
                    if count == 0:
                        break
                    else:
                        second += 1

                elif input_str[second] == "[":
                    count += 1
                    second += 1
                else:
                    second += 1

            index_mid = input_str.find("|")
            multiple = int(input_str[init+1:index_mid])
            left = func(input_str[index_mid+1:second])
            return input_str[:init] + func(multiple * left) + input_str[second+1:]





def main():
    str = input().strip()
    print(func(str))

main()

# print(func("HG[3|B[2|CA]]F"))

