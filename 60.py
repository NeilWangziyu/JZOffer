

def PrintProbability(n):
    global g_maxValue
    g_maxValue = 6

    if n < 1:
        return

    probability = [[0 for _ in range(g_maxValue * n + 1)], [0 for _ in range(g_maxValue * n + 1)]]

    flag = 0
    for i in range(1, g_maxValue+1):
        probability[flag][i] = 1
        # first time

    for k in range(2, n+1):
        for i in range(k):
            probability[1-flag][i] = 0

        for i in range(k, g_maxValue * k + 1):
            probability[1-flag][i] = 0
            j = 1
            while(j <= i and j <= g_maxValue):
                probability[1-flag][i] += probability[flag][i-j]
                j += 1
        flag = 1 - flag
    total = g_maxValue ** n
    for i in range(n, g_maxValue*n+1):
        ratio = probability[flag][i] /total
        print(i, ratio)

PrintProbability(2)