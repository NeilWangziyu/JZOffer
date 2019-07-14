def FirstNotRepeatingChar(string):
    if not string:
        return ""
    if len(string) == 1:
        return string

    from collections import Counter
    c = Counter(list(string))
    for i in string:
        if c[i] == 1:
            return i
    return  ""

print(FirstNotRepeatingChar("abaccdeff"))