def main():
    n = int(input().strip())
    villages = input().strip().split()
    villages = list(map(int, villages))
    i = 0
    j = 0
    while(i < len(villages) and villages[i]>=0):
        i += 1
    while(j < len(villages) and villages[j]<=0):
        j += 1


    total_use = 0
    # i:负数
    # j:正数
    while(i < len(villages) and j < len(villages)):
        # print(i, j)
        if abs(villages[i]) == abs(villages[j]):
            total_use += (abs(villages[i]) * abs(i-j))
            villages[i] = 0
            villages[j] = 0
            while (i < len(villages) and villages[i] >= 0):
                i += 1
            while (j < len(villages) and villages[j] <= 0):
                j += 1
        elif abs(villages[i]) > abs(villages[j]):
#             has more apply
            total_use += min(abs(villages[i]), abs(villages[j])) * abs(i-j)
            villages[i] = villages[i] + villages[j]
            villages[j] = 0
            while (j < len(villages) and villages[j] <= 0):
                j += 1
        else:
            # abs(villages[i]) < abs(villages[j]) 正的多
            total_use += min(abs(villages[i]), abs(villages[j])) * abs(i-j)
            villages[j] = villages[j] + villages[i]
            villages[i] = 0
            while (i < len(villages) and villages[i] >= 0):
                i += 1

    print(total_use)
main()

