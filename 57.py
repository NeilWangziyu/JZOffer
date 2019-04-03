def Findsum(nums, k):
    if not nums:
        return []
    if len(nums) == 0:
        return []
    init = 0
    last = len(nums)-1
    while(init < last):
        tem = nums[init] + nums[last]
        if tem == k:
            return [nums[init], nums[last]]
        else:
            if tem > k:
                last -= 1
            else:
                init += 1
    return  []

def FindContinueSequence(sum):
    if sum < 3:
        return []
    init = 1
    last = 2
    sum_now = 3
    res = []
    while(init < sum//2+1):
        if sum_now == sum:
            res.append([init, last])
            last += 1
            sum_now += last
        elif sum_now < sum:
            last += 1
            sum_now += last
        else:
            sum_now -= init
            init += 1

    return res

print(FindContinueSequence(sum=45))
