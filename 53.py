# /// --------------------
def getFirstK(data, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == k:
        if (mid > 0 and data[mid-1]!=k) or mid == 0:
            return mid
        else:
            end = mid - 1
    elif data[mid] > k:
        end = mid - 1
    else:
        start = mid + 1
    return getFirstK(data, start, end, k)


def getLastK(data, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == k:
        if (mid < len(data) - 1 and data[mid+1]!=k) or mid == len(data) - 1:
            return mid
        else:
            start = mid + 1
    elif data[mid] > k:
        end = mid - 1
    else:
        start = mid + 1
    return getFirstK(data, start, end, k)

def GetNumberOfK(data, k):
    if not data:
        return 0
    first = getFirstK(data, 0, len(data), k)
    last = getLastK(data, 0, len(data), k)
    if last > -1 and first > -1:
        return last - first + 1
    return 0


print(GetNumberOfK([1,2,3,4,4,4,4,4,5,6,7,8,9,10], 4))
print(GetNumberOfK([1,2,3,4,4,4,4,4,5,6,7,8,9,10], 10))



# /// --------------------
def GetMissingNumber(nums):
    if not nums:
        return -1
    left = 0
    right = len(nums)
    while(left <= right):
        mid = (left + right) // 2
        if mid == nums[mid]:
            left = mid + 1
        else:
            if mid == 0 or nums[mid-1] == mid - 1:
                return mid
            right = mid - 1
        if left == len(nums):
            return left
    return -1

print(GetMissingNumber([0,1,2,3,4,5,6,7, 8,9,10,11,12, 14]))




# /// --------------------
# 数值和下标相等的元素
def GetNumbersSameAsIndex(numbers):
    if not numbers:
        return -1
    left = 0
    right = len(numbers)
    while(left <= right):
        mid = (left + right) // 2
        if numbers[mid] == mid:
            return mid
        if numbers[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(GetNumbersSameAsIndex([-3,-1,1,3,5]))
