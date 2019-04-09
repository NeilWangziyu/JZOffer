def findMinumK(nums, k):
    if not nums:
        return []
    if len(nums) < k:
        return sorted(nums)
    else:
        i = nums[0]
        less = []
        more = []
        for each in nums[1:]:
            if each <= i:
                less.append(each)
            else:
                more.append(each)
        if len(less) == k:
            return less
        else:
            if len(less) > k:
                return findMinumK(less, k)
            else:
                return less + [i] + findMinumK(more, k - len(less) - 1)
def main():

    n_k = list(map(int, input().strip().split(' ')))
    n, k = n_k[0], n_k[1]
    nums = list(map(int, input().strip().split(' ')))

    less_nums = findMinumK(nums, k)
    less_nums.sort()
    lastnum = 0
    for i in range(len(less_nums)):
        print(less_nums[i] - lastnum)
        lastnum = less_nums[i]


# --------


import heapq
def main():
    n_k = list(map(int, input().strip().split(' ')))
    n, k = n_k[0], n_k[1]

    nums = list(map(int, input().strip().split(' ')))
    res = k - len(nums)
    nums = heapq.nsmallest(k, nums)
    nums.sort()

    lastnum = 0
    for i in range(len(nums)):
        print(nums[i] - lastnum)
        lastnum = nums[i]
    if res > 0:
        for i in range(res):
            print(0)
main()


# --------

def number3(num_list, k):
    tmp = num_list[:]
    if k < len(num_list):
        partitionOfK(tmp, 0, len(tmp) - 1, k)
        tmp = tmp[:k+1]
    res = k - len(num_list)  # 残差
    tmp.sort()
    lastnum = 0
    for i in range(len(tmp)):
        print(tmp[i] - lastnum)
        lastnum = tmp[i]
    if res > 0:
        for i in range(res):
            print(0)


def partitionOfK(numbers, start, end, k):
    if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
        return None
    low = start
    high = end
    key = numbers[start]
    while low < high:
        while low < high and numbers[high] >= key:
            high -= 1
        numbers[low] = numbers[high]
        while low < high and numbers[low] <= key:
            low += 1
        numbers[high] = numbers[low]
    numbers[low] = key
    if low < k:
        partitionOfK(numbers, start + 1, end, k)
    elif low > k:
        partitionOfK(numbers, start, end - 1, k)

number3(num_list=[5,5,7,2], k=1)
