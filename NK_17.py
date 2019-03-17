def main():
    N = int(input().strip())
    arr = list(map(int, input().split()))
    if N == 1:
        return abs(sum(arr))

    has_pos = False
    has_neg = False
    for each in arr:
        if each > 0:
            has_pos = True
        if each < 0:
            has_neg = True
    if has_pos and has_neg:
        arr = map(abs, arr)
        return sum(arr)
    else:
        arr = map(abs, arr)
        return sum(arr) - 2*min(arr)
main()

