def main():
    def jud(g, Li, M):
        sum = 0
        for each in Li:
            sum += (each//g)
        if sum >= M:
            return True
        else:
            return False

    N_M = input().strip().split(' ')
    N = int(N_M[0])
    M = int(N_M[1])
    Li = list(map(int, input().strip().split(' ')))
    l = 0
    r = 1000000000
    mid = 0
    for i in range(39):
        mid = (l + r) / 2
        if jud(mid, Li, M):
            l = mid
        else:
            r = mid
    print("%.2f" %mid)
main()