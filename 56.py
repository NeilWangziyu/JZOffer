def FindNumsAppearOnce(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    init = 0
    for each in nums:
        init = init ^ each
    return init

def FindNumsAppearOnce2(nums):
    # other appear three times
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    init = [0 for _ in range(32)]
    for each in nums:
        each_list = list(bin(each)[2:])[::-1]
        for i in range(len(each_list)):
            if each_list[i] == '1':
                init[i] += 1
    left = ['0' for _ in range(32)]
    for i in range(32):
        if init[i] % 3 != 0:
            left[i] = '1'
    left = left[::-1]
    return int("".join(left), 2)






print(FindNumsAppearOnce([0,0,1,1,2,2,3,4,4,5,5,6,6]))
print(FindNumsAppearOnce2([0,0,0,1,1,1,13,13,13,5,5,5,6,6,6,7,7,7,9,9,9,10,10,10,4,4,4,19]))