class TreeNode():
    def __init__(self, index):
        self.index = index
        self.leaves = []

NM = input().strip().split(" ")
N = int(NM[0])
M = int(NM[1])
matrix = {}
for i in range(M):
    input_Str = input().strip().split(" ")
    num = int(input_Str[0])
    root_index = int(input_Str[1])
    leave_list = input_Str[2:]
    leave_list = list(map(int, leave_list))
    matrix[root_index] = leave_list

print(matrix)


