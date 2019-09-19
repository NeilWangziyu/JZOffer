import json

# class Digraph():
#     def __init__(self, V):
#         # V：顶的个数
#         # E: 边的条数
#         # 利用数字来表示定点
#         self.V = V
#         self.mat = {}
#         self.E = 0
#         self.keys = []
#
#     def adj(self, v):
#         if v not in self.mat:
#             raise ValueError("v not in graph")
#         return self.mat[v]
#
#
#     def addEdge(self, v, w):
#         # from v to w
#         if v not in self.keys:
#             self.keys.append(v)
#
#         if v not in self.mat:
#             self.mat[v] = []
#         if w not in self.mat[v]:
#             self.mat[v].insert(0, w)
#             self.E += 1
#
#
#     def DirectedCycle(self):
#         #         利用DFS, return all cycles
#         def DFS_circle(index):
#             onStack[index] = True
#             marked[index] = True
#             # print(index, onStack, marked)
#             for w in self.adj(index):
#                 if onStack[w]:
#                     # print("find cycle")
#                     res_Tem = []
#                     x = index
#                     while (x != w):
#                         res_Tem.append(x)
#                         x = edgeTo[x]
#                     res_Tem.append(w)
#                     res_Tem.append(index)
#                     cycle.append(res_Tem)
#                 else:
#                     edgeTo[w] = index
#                     DFS_circle(w)
#             onStack[index] = False
#
#         marked = [False for _ in range(self.V)]
#         edgeTo = [-1 for _ in range(self.V)]
#         cycle = []
#         onStack = [False for _ in range(self.V)]
#         for i, v in enumerate(self.keys):
#             if marked[v] == False:
#                 DFS_circle(i)
#         # print(cycle)
#         return cycle

# dict = json.loads(input())
# length = len(dict.keys())
#
# key_list = list(dict.keys())
#
# tem = [[0 for _ in range(length)] for _ in range(length)]
#
# for each in dict.keys():
#     index1 = key_list.index(each)
#     for each_e in dict[each]:
#         index2 = key_list.index(each_e)
#         tem[index1][index2] = 1




# G = Digraph(length)
#
# for each in dict.keys():
#     for each_e in dict[each]:
#         G.addEdge(each, each_e)
#
# if G.DirectedCycle():
#     print(True)
# else:
#     print(False)

import json


def dfs(G, i, color):
    r = len(G)
    color[i] = -1
    is_DAG = 1
    for j in range(r):
        if G[i][j] != 0:
            # print j
            if color[j] == -1:
                is_DAG = 0
            elif color[j] == 0:
                is_DAG = dfs(G, j, color)
    color[i] = 1
    return is_DAG


def findcircle(G):
    r = len(G)
    color = [0] * r
    for i in range(r):
        # print i
        if color[i] == 0:
            is_DAG = dfs(G, i, color)
            if is_DAG == 0:
                break
    return is_DAG

dict_G = json.loads(input())
count = 0
symbol_ma = {}
for key, vals in dict_G.items():
    if key not in symbol_ma:
        symbol_ma[key] = count
        count += 1
    for val in vals:
        if val not in symbol_ma:
            symbol_ma[val] = count
            count += 1

r = len(symbol_ma)
G = [[0 for _ in range(r)] for _ in range(r)]
for key, vals in dict_G.items():
    row = symbol_ma[key]
    lines = [symbol_ma[v] for v in vals]
    for line in lines:
        G[row][line] = 1
is_DAG = findcircle(G)
if is_DAG == 0:
    print(True)
else:
    print(False)