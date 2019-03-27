def GettranslationCount(num):
    if num < 11:
        return 1
    num = str(num)
    length = len(num) - 1
    counts = [0 for _ in  range(len(num))]

    for i in range(length, -1, -1):
        count = 0
        if i < length:
            count = counts[i+1]
        else:
            count = 1

        if i < length:
            digit1 = ord(num[i]) - ord('0')
            digit2 = ord(num[i+1]) - ord('0')
            converted = digit1*10 + digit2
            if converted >= 10 and converted <= 25:
                if i < length - 2:
                    count += counts[i + 2]
                else:
                    count += 1
        counts[i] = count

    return counts[0]



print(GettranslationCount(12258))