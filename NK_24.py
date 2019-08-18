def main():
    n = int(input().strip())
    work_list = input().strip().split(" ")

    exes_list = input().strip().split(" ")

    dp = [0 for _ in range(n)]

    for i in range(n):
        if work_list[i] == "0" and exes_list[i] == "0":
            dp[i] = 0
        #     both close
        elif work_list[i] == "1" and exes_list[i] == "0":
            dp[i] = 1
#             only can work
        elif work_list[i] == "0" and exes_list[i] == "1":
            dp[i] = -1
        else:
            dp[i] = 2
#             both work and rest
    print(dp)
    res = [0 for _ in range(n+1)]
    res[0] = 0

    if dp[0] == 0:
        res[1] = 1
    else:
        res[1] = 0

    if (dp[0] == -1 and dp[1] == -1) or (dp[0] == 1 and dp[1] == 1):
        res[2] = 1
    elif dp[1] == 0:
        res[2] = res[1] + 1
    else:
        res[2] = res[1]


    for i in range(2, n+1):
        if dp[i-1] == 0:
            res[i] = res[i-1] + 1
        elif dp[i-1] == 1:
            if dp[i-2] == 1:
                res[i] = min(res[i-1], res[i-2] + 1)
            else:
                res[i] = res[i-1]
        elif dp[i-1] == -1:
            if dp[i-2] == -1:
                res[i] = min(res[i-1], res[i-2] + 1)
            else:
                res[i] = res[i-1]
        else:
            res[i] = min(res[i - 1], res[i - 2] + 1)

    print(res)
    print(res[-1])




main()