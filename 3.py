# 条件太狭窄
def duplicate(nums):
    if not nums:
        return None
    for i in range(len(nums)):
        while(nums[i]!=i):
            m = nums[i]
            if nums[m] == m:
                print("find")
                return m
            else:
                nums[m], nums[i] = nums[i], nums[m]
    return "no result"

def duplicate2(nums):
    # binary search

    def countRange(nums, start, end):
        if not nums:
            return 0
        count = 0
        for each in nums:
            if each >= start and each <= end:
                count += 1
        print(start, end, count)
        return count

    if not nums:
        return None
    lo = min(nums)
    hi = max(nums)
    while(lo<=hi):
        mid = (lo + hi) // 2
        this_count = countRange(nums, lo, mid)
        if lo == mid:
            if this_count > 1:
                return lo
        if this_count > mid - lo + 1:
            hi = mid
        else:
            lo = mid + 1
    return "no result"




if __name__ == "__main__":
    print("hello")
    test = [2,3,1,0,2,5,3]
    print(duplicate(test))
    test2 = [1,5,4,3,2,6,7,8,9,9,10,11]
    print(duplicate2(test2))
