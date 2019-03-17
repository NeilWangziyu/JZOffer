def main():
    import math
    N_M = input().strip().split(' ')
    n, k = int(N_M[0]), int(N_M[1])
    arr = list(map(int, input().split()))
    a = min(arr)
    sum = 0
    for i in range(n):
        sum += arr[i] - a
    print(math.ceil(sum / k))

main()
