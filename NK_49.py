N = int(input())
ci = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 0

prev_map = {}
prev_map[ci[0]] = 0

for i in range(1, N):
    i_same = i
    if ci[i] not in prev_map:
        prev_map[ci[i]] = i
        dp[i] = dp[i-1] + 1
    else:
        j = prev_map[ci[i]]
        dp[i] = min(dp[i-1]+1, dp[j]+1)
        prev_map[ci[i]] = i

print(dp[-1])

