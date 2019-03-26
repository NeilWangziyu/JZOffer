string = '0123456789101112131415....'


def countOfIntegers(digits):
    if digits == 1:
        return 10
    count = 10 ** (digits-1)
    return 9 * count

def beginNumber(digits):
    if digits == 1:
        return 0
    else:
        return 10 ** (digits - 1)

def digitAtN(index, digits):
    number = beginNumber(digits) + index // digits
    indexFromRight = digits - index % digits
    for i in range(1, indexFromRight):
        number //= 10
    return number % 10



def digitAtIndex(index):
    if index < 0:
        return -1
    digits = 1
    # digits:位数
    while(True):
        number = countOfIntegers(digits)
        if index < number * digits:
            return digitAtN(index, digits)

        index -= digits * number
        digits += 1

print(digitAtIndex(1003))
