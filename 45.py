def printMinNumber(numbers):
    if not numbers:
        return 0
    if len(numbers) == 1:
        return numbers[0]

    def compare(num1, num2):
        # True:means num1 should be back
        check1 = int(str(num1) + str(num2))
        check2 = int(str(num2) + str(num1))
        if check1 > check2:
            return False
        else:
            return True

    def qsort(numbers):
        if not numbers:
            return []
        if len(numbers) == 1:
            return numbers
        init = numbers[0]
        left = []
        right = []
        for each in numbers[1:]:
            if compare(init, each):
                right.append(each)
            else:
                left.append(each)
        return qsort(left) + [init] + qsort(right)

    numbers = map(str, qsort(numbers))


    return "".join(numbers)



if __name__ == "__main__":
    numbers = [3, 32, 321, 11, 9]
    print(printMinNumber(numbers))