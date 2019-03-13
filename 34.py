class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    res = []
    def FindPath(self, root, value):

        def FindPathDFS(root, exceptSum, path, currentSum):
            if not root:
                return
            currentSum += root.val
            path += [root.val]
            if currentSum == exceptSum:
                if not root.left and not root.right:
                    self.res.append(path)
            if root.left:
                FindPathDFS(root.left, exceptSum, path, currentSum)
            if root.right:
                FindPathDFS(root.right, exceptSum, path, currentSum)


        if not root:
            return []
        currentSum = 0
        FindPathDFS(root, value, [], currentSum)
        return self.res

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)

    s = Solution()
    print(s.FindPath(root, 22))
