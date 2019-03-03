def PowerWithUnsignedExponent(base, exp):
    if exp == 0:
        return 1
    if base == 1:
        return base

    if exp < 0:
        flag = -1
        exp = - exp
    else:
        flag = 1


    result = PowerWithUnsignedExponent(base, exp>>1)
    result *= result
    if exp & 1 == 1:
        result *= base

    if flag == 1:
        return result
    else:
        return 1/result



if __name__ == "__main__":
    base = 10
    exp = -5
    print(PowerWithUnsignedExponent(base, exp))
