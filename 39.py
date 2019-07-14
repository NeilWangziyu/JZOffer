class Solution():
    def MoreThanHalfNum(self, nums):
        # nlog(n)
        def partition(nums, start, end):
            check_num = nums[start]
            left = []
            right = []
            for i in range(start, end):
                if nums[i] > check_num:
                    right.append(nums[i])
                else:
                    left.append(nums[i])
            return len(left)

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        start = 0
        end = len(nums) - 1
        length = len(nums)
        index = partition(nums, start, end)

        while(index != mid):
            if index > mid:
                index = partition(nums, start, index-1)
            else:
                index = partition(nums, index+1, end)

        # here should
        return nums[index]


    def MoreThanHalfNum2(self, nums):
        result = nums
        time = 1
        for i in range(1, len(nums)):
            if time == 0:
                result = nums[i]
                time = 1
            else:
                if result == nums[i]:
                    time += 1
                else:
                    time -= 1
        return result






if __name__ =="__main__":
    s = Solution()
    nums = [1,2,3,2,2,2,5,4,2]
    print(s.MoreThanHalfNum(nums))
    print(s.MoreThanHalfNum2(nums))