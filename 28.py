# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(self, root: TreeNode) -> bool:
    """
    interesting point：构造两种遍历方法
    :param root:
    :return:
    """

    def isSymmetric_core(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        else:
            return isSymmetric_core(root1.left, root2.right) and isSymmetric_core(root1.right, root2.left)

    return isSymmetric_core(root, root)
