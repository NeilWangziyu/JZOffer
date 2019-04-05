# interview one and two
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# 两道tree的题目，分别用递归和非递归实现
class Solution():
    checked = []

    def preorder_tree(self, root, value):
        if not root:
            return root
        if root.val == value:
            return root
        else:
            if root.val > value:
                return self.preorder_tree(root.left, value)
            else:
                return self.preorder_tree(root.right, value)


    def get_depth(self, root):
        if not root:
            return 0
        else:
            left = self.get_depth(root.left)
            right = self.get_depth(root.right)
            return 1 + max(left, right)

    def find_longest_continue(self, grid):
        def DFS(r_i, c_j):
            if grid[r_i][c_j] != 1 or self.checked[r_i][c_j] == True:
                return 0
            else:
                self.checked[r_i][c_j] = True
                if r_i > 0:
                    left = DFS(r_i-1, c_j)
                else:
                    left = 0

                if r_i < row-1:
                    right = DFS(r_i+1, c_j)
                else:
                    right = 0

                if c_j > 0:
                    up = DFS(r_i, c_j-1)
                else:
                    up = 0

                if c_j < col - 1:
                    down = DFS(r_i, c_j-1)
                else:
                    down = 0
                return 1 + up + down + left + right


        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        self.checked = [[False for  _ in range(col)] for _ in range(row)]
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and self.checked[i][j] == False:
                    check_result = DFS(i, j)
                    count = max(count, check_result)
        return count


if __name__ == "__main__":
    grid = [[0,1,1,1,0],[0,1,0,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,1,1]]
    s = Solution()
    print(s.find_longest_continue(grid))