# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirrorrecursizely(self,root):
        if not root:
            return
        if not root.left and not root.right:
            return

        tem = root.left
        root.left = root.right
        root.right = tem

        if root.left:
            self.Mirrorrecursizely(root.left)
        if root.right:
            self.Mirrorrecursizely(root.right)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    s.Mirrorrecursizely(root)
    print(root.val)
    print(root.left.val)
    print(root.left.left.val)
    print(root.left.right.val)



