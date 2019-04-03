# 两次翻转
def reverse_word(string):
    if not string:
        return ""

    if len(string) == 1:
        return string

    res = []
    tem = ""

    for i in range(len(string) - 1, -1, -1):
        if string[i] == ' ':
            if tem:
                res.append(tem)
            tem = ""
        else:
            # tem += string[i]  之前写出了bug
            tem = string[i] + tem

    if tem:
        res.append(tem)

    return " ".join(res)


def reverse_word2(string):
    if not string:
        return ""
    if len(string) == 1:
        return string

    def reverse(start, end, string_list):
        # % reverse content between start and end
        while(start <= end):
            tem = string_list[start]
            string_list[start] = string_list[end]
            string_list[end] = tem
            start += 1
            end -= 1
        return string_list

    string_list = list(string)
    string_list_reverse = reverse(0, len(string_list)-1, string_list)
    i = 0
    for j in range(i, len(string_list_reverse)):
        if string_list_reverse[j] == ' ':
            string_list_reverse = reverse(i, j - 1, string_list_reverse)
            i = j + 1
    if len(string_list_reverse) - i > 1:
        string_list_reverse = reverse(i, len(string_list_reverse) - 1, string_list_reverse)
    return "".join(string_list_reverse)

string = "today is a good day we really like it"
print(reverse_word(string))
print(reverse_word2(string))


