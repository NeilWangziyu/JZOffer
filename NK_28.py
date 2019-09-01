def find_k(arr, k):
    if len(arr) == 1:
        return arr[0]
    init = arr[0]
    large = []
    low = []
    for each in arr[1:]:
        if each > init:
            large.append(each)
        else:
            low.append(each)

    if len(large) == k-1:
        return init
    elif len(large) > k - 1:
        return find_k(large, k)
    else:
        return find_k(low, k - (len(large) - 1))


def main():
    nmk = input().strip().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])

    sore = []
    for i in range(n+1):
        for j in range(m+1):
            sore.append(i*j)
    print(sore)

    print(find_k(sore, k))
main()

#
# def find_k(arr, k):
#     init = arr[0][0]
#     large = []
#     low = []
#     for each in arr[1:]:
#         if each[0] > init:
#             large.append(each)
#         else:
#             low.append(each)
#
#     if len(low) == k-1:
#         return init
#     elif len(low) > k - 1:
#         return find_k(low, k)
#     else:
#         return find_k(large, k - (len(low) - 1))
#
#
#
def main():
    nmk = input().strip().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    if n > m:
        m, n = n, m

    has_been = set()

    if k < (n * m) // 2:
        heap = [(m * n, m, n)]
        for i in range(k):
            res = heap.pop(0)
            if res[1] > 1:
                tmpm = res[1] - 1
                tmpn = res[2]
                if (tmpm, tmpn) not in has_been:
                    has_been.add((tmpm, tmpn))
                    heap.append((tmpm * tmpn, tmpm, tmpn))
            if res[2] > 1:
                tmpm = res[1]
                tmpn = res[2] - 1
                if (tmpm, tmpn) not in has_been:
                    has_been.add((tmpm, tmpn))
                    heap.append((tmpm * tmpn, tmpm, tmpn))
            heap.sort(reverse=True, key=lambda i: i[0])
    else:
        k = n * m - k + 1
        heap = [(1, 1, 1)]
        for i in range(k):
            res = heap.pop(0)
            if res[1] < m + 1:
                tmpm = res[1] + 1
                tmpn = res[2]
                if (tmpm, tmpn) not in has_been:
                    has_been.add((tmpm, tmpn))
                    heap.append((tmpm * tmpn, tmpm, tmpn))
            if res[2] < n + 1:
                tmpm = res[1]
                tmpn = res[2] + 1
                if (tmpm, tmpn) not in has_been:
                    has_been.add((tmpm, tmpn))
                    heap.append((tmpm * tmpn, tmpm, tmpn))
            heap.sort(key=lambda i: i[0])
    print(res[0])
main()