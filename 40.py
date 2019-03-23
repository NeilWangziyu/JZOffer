def GestLeastNumbers(input, n, k):

    def Partition(input, start, end, k):
        checked_num = input[k-1]
        begin = input[:start]
        last = input[end+1:]
        less = []
        more = []
        for i in range(start, end+1):
            if i != k-1:
                if input[i] <= checked_num:
                    less.append(input[i])
                else:
                    more.append(input[i])
        re_input = begin + less + [checked_num] + more + last
        return len(begin) + len(less) , re_input

    if k == 0:
        return []
    if not input:
        return []
    if k >= n :
        return input

    start = 0
    end = n - 1
    index, input = Partition(input, start, end, k)
    while(index != k-1):
        if index > k - 1:
            end = index - 1
            index, input = Partition(input, start, end, k)
        else:
            start = index + 1
            index, input = Partition(input, start, end, k)
    return input[:k]


if __name__ == "__main__":
    input = [4,5,1,6,2,7,3,8, 10, 11, 0, -1, 91]
    k = 3
    print(GestLeastNumbers(input, len(input), k))
