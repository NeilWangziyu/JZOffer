# different kinds of sort algorithm of Python
# must finished it with best time and space effeciency

test1 = [-1,1,2,3,9,8,7,0,1,4,5,7,11,12,99]
test2 = []
test3 = [0]
test4 = [1,1,1,1,1,1,1,2,2,2,4,4,5,6,7]


# quick sort
# 0: my old quick sort, has too much space
def quick_sort0(arr):
    if not arr:
        return arr
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort0(left) + [pivot] + quick_sort0(right)



def quick_sort(arr):
    def quick_sort_core(arr, start, end):
        # 递归的退出条件
        if start >= end:
            return
        # 设定起始元素为要寻找位置的基准元素
        mid = arr[start]
        # low为序列左边的由左向右移动的游标
        low = start
        # high为序列右边的由右向左移动的游标
        high = end

        while low < high:
            # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
            while low < high and arr[high] > mid:
                high -= 1
            # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
            while low < high and arr[low] <= mid:
                low += 1
            # 交换
            arr[low], arr[high] = arr[high], arr[low]

        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
        # 将基准元素放到该位置
        arr[start], arr[low] = arr[low], arr[start]
        # 对基准元素左边的子序列进行快速排序
        quick_sort_core(arr, start, low - 1)
        # 对基准元素右边的子序列进行快速排序
        quick_sort_core(arr, low + 1, end)

    if not arr:
        return arr
    if len(arr) < 2:
        return arr
    quick_sort_core(arr, 0, len(arr)-1)
    return arr

# ----another idea
def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j]<=x: # 如果将这里修改为A[j] > x，则为降序排列
            i += 1
            A[i],A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def QUICKSORT_ASC(A, p, r):
    if p < r:
        q = PARTITION(A, p, r) # 此时下标为q的值已经确定了，后面的排序应该排除它
        QUICKSORT_ASC(A, p, q - 1)
        QUICKSORT_ASC(A, q + 1, r)


# 堆排序
# 创建一个堆 {\displaystyle H[0..n-1]} {\displaystyle H[0..n-1]}
# 把堆首（最大值）和堆尾互换
# 把堆的尺寸缩小1，并调用shift_down(0),目的是把新的数组顶端数据调整到相应位置
# 重复步骤2，直到堆的尺寸为1
def heap_sort(arr):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

# 创建最大堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(start, len(arr) - 1)

    print("max heap:", arr)

# 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        # 不断缩小堆大小
        sift_down(0, end - 1)

    return arr



# 归并排序


# others




if __name__ == "__main__":
    print(quick_sort0(test1))
    print(quick_sort0(test2))
    print(quick_sort0(test3))
    print(quick_sort0(test4))
    print(quick_sort(test1))
    print(quick_sort(test2))
    print(quick_sort(test3))
    print(quick_sort(test4))


    print(heap_sort(test1))
    print(heap_sort(test2))
    print(heap_sort(test3))
    print(heap_sort(test4))