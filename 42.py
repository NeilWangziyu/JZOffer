def findGreatestSumOfSubArray(nums):
    "最长连续子集"
    if not nums:
        return 0
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)



if __name__ == "__main__":
    s = [1,2,3,-4,5,7, -10, 10, 12,1,-4,-9,-7, -11]
    print(findGreatestSumOfSubArray(s))


    s = [1, -2, 3, 10, -4, 7, 2, -5]
    print(findGreatestSumOfSubArray(s))