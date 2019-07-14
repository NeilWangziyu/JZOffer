def main():
    n_a = input().strip().split(' ')
    n = int(n_a[0])
    a = int(n_a[1])



    nums = input().strip().split(' ')
    nums = list(map(int, nums))

    if n == 1: return 0
    if n == 2:
        return min(abs(a - nums[0]), abs(a - nums[1]))


main()





