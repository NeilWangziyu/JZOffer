def min_num(numbers):
    low = 0
    high = len(numbers)-1
    mid = 0
    while(numbers[high] <= numbers[low]):
        if high - low == 1:
            mid = high
            break
        mid = (high + low) // 2

        if numbers[mid] == numbers[high] and numbers[mid] == numbers[low]:
            # 这一种特殊情况，三者全部相同
            return  MinINOrder(numbers, low, high)

        if numbers[mid] >= numbers[low]:
            low = mid
        else:
            high = mid
    return numbers[mid]


def MinINOrder(numbers, low, high):
    print(low, high)
    min = float('inf')
    for i in range(low, high+1):
        if numbers[i] < min:
            min = numbers[i]
    return min




if __name__ == "__main__":
    # numbers = [3,4,5,6,7,8,1,2]
    numbers = [1,1,1,0,1]

    print(min_num(numbers))