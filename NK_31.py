def main():
    nm = input().strip()
    n = int(nm[0])
    m = int(nm[1])
    each_list = input().strip().split()
    each_list = list(map(int, each_list))

    total = 0
    for i in range(1, n+1):
        total += n*(each_list[n-1])
    print(total // m + 1)
main()
