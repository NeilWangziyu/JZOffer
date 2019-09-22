class Solution:
    length = float("inf")
    def find_minest(self, N, ways, C):
        checked = [False for _ in range(N)]
        checked[0] = True
        len = 0
        for each in ways[0]:
            # print(each)
            checked[each[0]] = True
            self.DFS(each[0], N-1, checked, C - each[2], len + each[1])
            checked[each[0]] = False
        if self.length == float("inf"):
            return -1
        else:
            return self.length


    def DFS(self, index, e, checked, left_money, road):
        if left_money < 0:
            return

        if (index == e):
            if road < self.length:
                self.length = road
        else:
            for each in ways[index]:
                # print(each)
                if checked[each[0]] == False:
                    checked[each[0]] = True
                    left_money -= each[2]
                    road += each[1]
                    self.DFS(each[0], N - 1, checked, left_money, road)
                    checked[each[0]] = False
                    left_money += each[2]
                    road -= each[1]
        return


NMC = input().strip().split()
N = int(NMC[0])
M = int(NMC[1])
C = int(NMC[2])

ways = {}

for i in range(M):
    input_str = list(map(int, input().strip().split()))
    start = input_str[0]
    end = input_str[1]
    legth = input_str[2]
    price = input_str[3]
    if start not in ways:
        ways[start] = [[end, legth, price]]
    else:
        ways[start].append([end, legth, price])
# print(ways)
s = Solution()
print(s.find_minest(N, ways, C))





