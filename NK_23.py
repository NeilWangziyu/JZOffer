def main():
    n = int(input().strip())
    low_list = input().strip().split(" ")
    low_list = list(map(int, low_list))
    # left_high = [-1 for _ in range(n)]
    # right_high = [-1 for _ in range(n)]
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    for i in range(n):
        if i > 0:
            cover = -1
            left_C = 0
            for t in range(i-1, -1, -1):
                if low_list[t] > cover:
                    left_C += 1
                    cover = low_list[t]
            left[i] = left_C
        if i < len(low_list) - 1:
            cover = -1
            right_C = 0
            for t in range(i + 1, len(low_list)):
                if low_list[t] > cover:
                    right_C += 1
                    cover = low_list[t]
            right[i] = right_C
    res = []

    for i in range(n):
        res.append(str(left[i] + right[i] + 1))
    print(" ".join(res))
main()
