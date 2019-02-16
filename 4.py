def Find(nums, key):
    if nums == [[]]:
        return None

    col = len(nums[0])
    row = len(nums)
    init = [0, col-1]
    while(nums[init[0]][init[1]] != key):
        if nums[init[0]][init[1]] > key:
            init = [init[0], init[1]-1]
        elif nums[init[0]][init[1]] < key:
            init = [init[0]+1, init[1]]

        if init[0] > row-1 or init[1] < 0:
            return  False

    if nums[init[0]][init[1]] == key:
        return True
    else:
        return False



if __name__ == "__main__":
    nums = [[1,2,8,9], [2,4,9,12], [4, 7, 10, 13]]
    key = 3
    print(Find(nums, key))