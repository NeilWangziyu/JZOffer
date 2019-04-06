def MaxInWindow(nums, k):
    if not nums:
        return []
    if k <= 0:
        return []
    if len(nums) < k:
        return None
    check_list = []
    for i in range(k):
        while(check_list and nums[check_list[-1]]<nums[i]):
            check_list.pop()
        check_list.append(i)
    max_list = [nums[check_list[0]]]
    for i in range(k, len(nums)):
        while(check_list and nums[check_list[-1]]<nums[i]):
            check_list.pop()
        if check_list and check_list[0] <= i-k:
            check_list.pop(0)
        check_list.append(i)
        max_list.append(nums[check_list[0]])
    return max_list

print(MaxInWindow(nums=[2,3,4,2,6,2,5,1], k=3))
# 队列最大值

class InternalData():
    def __init__(self, value, index):
        self.val = value
        self.index = index

class QueueWithMax():
    def __init__(self):
        self.currentIndex = 0
        self.maximums = []
        self.data = []

    def push_back(self, number):
        while(self.maximums and number >= self.maximums[-1].value):
            self.maximums.pop(-1)
        this_data = InternalData(value=number, index=self.currentIndex)
        self.data.append(this_data)
        self.maximums.append(this_data)
        self.currentIndex += 1

    def pop_front(self):
        if not self.maximums:
            return "error"
        if self.maximums[0].index == self.data[0].index:
            self.maximums.pop(0)
        self.data.pop(0)


    def queue_max(self):
        if not self.maximums:
            return "error"
        else:
            return self.maximums[0]

