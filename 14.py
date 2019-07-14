def maxProductAfterCutting(length):
    if length == 2:
        return 1
    if length == 3:
        return 2

    Dp = [0 for _ in range(length+1)]
    Dp[2] = 1
    Dp[3] = 2
    for i in range(4, length+1):
        for j in range(2, i):
            Dp[i] = max(max(j*(i-j), Dp[j]*(i-j)), Dp[i])
    return Dp[-1]


def maxProductAfterCutting2(length):
    """
    greedy
    """
    if length == 2:
        return 1
    if length == 3:
        return 2
    if length == 4:
        return 4
    timesOF3 = length //3
    if length - timesOF3 * 3 == 1:
        timesOF3 -= 1
    timesOF2 = (length - timesOF3*3) / 2
    return int(3**timesOF3 * 2**timesOF2)



if __name__ == "__main__":
    length = 15
    # length > 1
    print(maxProductAfterCutting(length))
    print(maxProductAfterCutting2(length))