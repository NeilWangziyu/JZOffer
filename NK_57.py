def maxEnvelopes(envelopes) -> int:
    size = len(envelopes)

    envelopes.sort(key=lambda x: x[0]*x[1])

    dp = [[1,1] for _ in range(size)]
    dp2 = [[1,1] for _ in range(size)]

    res = [0,0]

    for i in range(size):
        for j in range(i):
            if (envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]) or (envelopes[i][1] > envelopes[j][0] and envelopes[i][0] > envelopes[j][1]):
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        tem  = 0
        for j in range(i):
            if dp[j][0] == dp[i][0] - 1 and (envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]) or (envelopes[i][1] > envelopes[j][0] and envelopes[i][0] > envelopes[j][1]):
                tem += dp[j][1]
        if tem == 0:
            tem = 1
        dp[i][1] = tem
        if dp[i][0] > res[0]:
            res[0] = dp[i][0]
            res[1] = dp[i][1]
    print(dp)
    tt = 0
    for each in dp:
        if each[0] == res[0]:
            tt += each[1]
    return tt % 1000000007


n = int(input().strip())
envelop = []
for _ in range(n):
    ab = list(map(int, input().strip().split()))
    envelop.append(ab)
print(maxEnvelopes(envelop))


