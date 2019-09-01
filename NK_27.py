# def main():
#     n = int(input().strip())
#     list_N = input().strip().split(" ")
#     input_list = list(map(int, list_N))
#
#     dp = [[0 for _ in range(51)] for _ in range(n+1)]
# #     dp:i:0 - 50
#     for i in range(1, n+1):
#         number = input_list[i-1]
#         for j in range(1, number+1):
#             if i == 1:
#                 dp[i][j] = 1/number
#             else:
#                 dp[i][j] += dp[i-1][j] * j / number
#                 for k in range(j+1, number+1):
#                     dp[i][k] += dp[i-1][j] * 1/number
#
#     res = 0
#     print(dp)
#     for k in range(n+1):
#         res += dp[n][k]*k
#     print(res)
# main()
#


# coding:utf-8
import sys
string1 = sys.stdin.readline().rstrip()
N = int(string1)

string2 = sys.stdin.readline().rstrip()
string2 = string2.split(' ')

kinds = list(map(lambda x:int(x),string2))

max_kinds = max(kinds)

pcf = [1 for i in range(max_kinds)]

pcf.insert(0,0)

for kind in kinds:
    step = 1/kind
    for i in range(1, kind+1):
        pcf[i] *= step*i

pdf = pcf[:]
for i in range(1,max_kinds+1):
    pdf[i]=pcf[i]-pcf[i-1]

expect = 0

for i in range(1,max_kinds+1):
    expect+=i*pdf[i]


print('%.2f' %expect)