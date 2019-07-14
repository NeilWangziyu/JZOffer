def main():
    n = int(input().strip())
    tower = [0]
    for i in range(n):
        tower.append(int(input().strip()))
    DP_pa = [0 for _ in range(n+1)]
    DP_fei = [0 for _ in range(n+1)]

    DP_pa[0] = 0
    DP_fei[0] = 0
    for i in range(1, n+1):
        if i > 2:
            DP_fei[i] = min(DP_pa[i-1], DP_pa[i-2])
            DP_pa[i] = min(DP_fei[i-1]+tower[i], DP_pa[i-1]+tower[i])
        else:
            DP_fei[i] = 0
            DP_pa[i] = min(DP_fei[i-1]+tower[i], DP_pa[i-1]+tower[i])

    print(min(DP_fei[-1], DP_pa[-1]))

main()





