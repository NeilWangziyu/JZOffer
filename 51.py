# def InversePairs(nums):
#     if not nums:
#         return 0
#     start = 0
#     end = len(nums) - 1
#     copy = [nums[i] for i in range(len(nums))]
#     count = InversePairsCore(nums, copy, start, end)
#
#     return count
#
#
# def InversePairsCore(nums, copy, start, end):
#     if start == end or end - start == 1:
#         copy = nums
#         return nums, 0
#
#
#     length = (end - start) // 2
#     # here, nums is sorted
#     nums, left = InversePairsCore(nums, copy, start, start + length)
#     nums, right = InversePairsCore(nums, copy, start+length, end)
#
#
#     i = start + length
#     j = end
#     count = 0
#     new_nums = []
#
#     while(i >= start and j >= start+length+1):
#         if nums[i] > nums[j]:
#             new_nums.insert(0, nums[i])
#             i -= 1
#             count += j - start - length
#         else:
#             new_nums.insert(0, nums[j])
#
#     while(i >= start):
#         new_nums.insert(0, nums[i])
#         i -= 1
#     while(j >= start+length+1):
#         new_nums.insert(0, nums[j])
#         j -= 1
#     return new_nums, left+right+count


class Solution():
    def InversePairs(self, data):
        sortData = sorted(data)
        count = 0
        for i in sortData:
            pos = data.index(i)
            count += pos
            data.pop(pos)
        return count

    def quick_sort(self, data):
        if len(data) < 2:
            return data
        left = self.quick_sort([i for i in data[1:] if i <= data[0]])
        right = self.quick_sort([j for j in data[1:] if j > data[0]])
        return left + [data[0]] + right



    # -----
    def InversePairs2(self, data):
        return self.sort(data[:], 0, len(data) - 1, data[:])

    def sort(self, temp, left, right, data):
        if right - left < 1:
            return 0
        if right - left == 1:
            if data[left] < data[right]:
                return 0
            else:
                temp[left], temp[right] = data[right], data[left]
                return 1

        mid = (left + right) // 2

        res = self.sort(data, left, mid, temp) + self.sort(data, mid + 1, right, temp)
        i = left
        j = mid + 1
        index = left

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                res += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= right:
            temp[index] = data[j]
            j += 1
            index += 1
        return res




s = Solution()

print(s.InversePairs([7,5,6,4]))
print(s.InversePairs2([7,5,6,4]))