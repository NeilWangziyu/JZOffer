# 二叉树的深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def TreeDepth(self, root):
        if not root:
            return 0
        nleft = self.TreeDepth(root.left)
        nright = self.TreeDepth(root.right)
        return max(nleft, nright) + 1

    # leetcode110
    def IsBalance(self, root):
        if not root:
            return True
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalance(root.left) and self.IsBalance(root.right)

    def IsBalanceOneTime(self, root):
        def balanced(root):
            if not root:
                return 0
            left = balanced(root.left)
            right = balanced(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return balanced(root) != -1
