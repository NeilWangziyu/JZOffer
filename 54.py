# 二叉搜索树第K大节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def KthNode(root, k):
    if not root or k<=0:
        return -1
    return KthNodeCore(root, k)


def KthNodeCore(root, k):
    if not root:
        return None

    tree_stack = []
    while (root or tree_stack):
        if root:
            tree_stack.append(root)
            root = root.left
        else:
            root = tree_stack.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right
    return -1

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(KthNode(root, 6))