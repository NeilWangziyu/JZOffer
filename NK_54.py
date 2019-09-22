n = int(input())
for _ in range(n):
    num = int(input())
    check = input().strip().split()
    check_list = list(map(int, check))
    total_sum = sum(check_list)
    check_list.sort()

    dp = [[False for _ in range(total_sum//2+1)] for _ in range(num//2+1)]
    dp[0][0] = True
    for k in range(0, num):
        for i in range(min(k, num//2), 0, -1):
            for j in range(total_sum//2+1):
                if (j >= check_list[k] and dp[i - 1][j - check_list[k]]):
                    dp[i][j] = True
    for e in range(total_sum // 2, -1, -1):
        if(dp[num//2][e]):
            print(e, total_sum - e)
            break


