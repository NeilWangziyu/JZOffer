# https://leetcode-cn.com/problems/minimum-path-sum/
def getMaxValue(grid):
    if not grid:
        return 0
    row = len(grid)
    col = len(grid)

    dp = [[-1 for _ in range(row)] for _ in range(col)]
    dp[0][0] = grid[0][0]
    for i in range(1, col):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1, row):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[row-1][col-1]

def getMaxValue2(grid):
    # less space
    if not grid:
        return 0
    row = len(grid)
    col = len(grid)
    dp = [0 for _ in range(col)]
    for j in range(0, row):
        for i in range(0, col):
            if i == 0:
                dp[i] = dp[i] + grid[i][j]
            else:
                dp[i] = max(dp[i], dp[i-1]) + grid[i][j]

    return dp[-1]







if __name__ == "__main__":
    grid = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(getMaxValue(grid))
    print(getMaxValue2(grid))