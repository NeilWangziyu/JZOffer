def isNumeric(str):
    if not str:
        return False
    else:
        pass










if __name__ == "__main__":
    print(isNumeric("+100"))
    print(isNumeric("+10e1"))
    print(isNumeric("-123"))
    print(isNumeric("3.14"))
    print(isNumeric("+-5"))
    print(isNumeric("12e+5.4"))
    print(isNumeric("-1E-16"))

