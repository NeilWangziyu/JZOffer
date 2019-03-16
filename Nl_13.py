def main():

    N = int(input().strip())
    for i in range(N):
        num = int(input().strip())
        tem = [1] * (N+1)

        min_i = num.index(min(num))
        num = num[min_i:] + num[:min_i]

        for i in range(1, N+1):
            if num[i] > num[i-1]:
                num[i] = num[i-1] + 1
        for i in range(N-1, -1, -1):
            if num[i] > num[i+1]:
                tem[i] = max(tem[i], tem[i+1] + 1)
        tem[0] = min(tem[0], tem[N])
        print(sum(tem))

main()


    # leetcode 贪心思路：
    # def candy(ratings):
    #     candies = [1 for i in range(len(ratings))]
    #     for i in range(len(ratings) - 1):
    #         if ratings[i + 1] > ratings[i]:
    #             candies[i + 1] = candies[i] + 1
    #     for i in range(len(ratings) - 1, 0, -1):
    #         if ratings[i - 1] > ratings[i]:
    #             candies[i - 1] = max(candies[i - 1], candies[i] + 1)
    #     return candies
