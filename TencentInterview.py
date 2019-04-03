# Q: 快排


def quick_sort(list_t):
    if not list_t:
        return []

    if len(list_t) == 1:
        return list_t

    init = list_t[0]

    less = []
    more = []

    for each in list_t[1:]:
        if each <= init:
            less.append(each)
        else:
            more.append(each)
    return quick_sort(less) + [init] + quick_sort(more)


# Q： reverse
# words
# exmaple: "Hello world. 123 !"  -> "! 123 world. Hello"

# JZ offer 58
# 两个..都有bug
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
            # tem += string[i]
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
        if end - start == 1:
            return string_list
        for index in range(start, start + (end - start) // 2):
            tem = string_list[index]
            string_list[index] = string_list[end - index]
            string_list[end - index] = tem
        return string_list

    string_list = list(string)
    string_list_reverse = reverse(0, len(string_list), string_list)
    i = 0
    for j in range(1, len(string)):
        if string[j] != ' ':
            pass
        else:
            string_list_reverse = reverse(i, j, string_list_reverse)
            i = j

    if j - i > 1:
        string_list_reverse = reverse(i, j, string_list_reverse)
    return "".join(string_list_reverse)