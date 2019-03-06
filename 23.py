def reorderOddEven(str):
    if len(str) <= 1:
        return str

    lo = 0
    hi = len(str) - 1
    while(lo <= hi):
        while(str[lo] % 2 != 0):
            lo += 1
        while (str[hi] % 2 == 0):
            hi -= 1

        if lo < hi:
            str[lo], str[hi] = str[hi], str[lo]

    return str

def ReOrder(fun, str):
    if len(str) <= 1:
        return str
    lo = 0
    hi = len(str) - 1
    while(lo < hi):
        while(lo<hi and fun(str[lo])):
            lo += 1
        while(lo < hi and fun(str[hi])):
            hi -= 1
        if lo < hi:
            str[lo], str[hi] = str[hi], str[lo]
    return str

def func(num):
    return num & 1 == 0



if __name__ =="__main__":
    str = [1,2,3,4,5,6,7,8 ]
    print(reorderOddEven(str))
    print(ReOrder(func, str))