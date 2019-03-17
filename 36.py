# from BST to ListNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def ConvertNode(self, root, lastnode):
        if not root:
            return lastnode
        current = root
        if current.left:
            lastnode = self.ConvertNode(root.left, lastnode)
        current.left = lastnode
        if lastnode:
            lastnode.right = current
        lastnode = current
        if current.right:
            lastnode = self.ConvertNode(root.right, lastnode)
        return lastnode


    def Convert(self, RootOfTree):
        LastNodeInList = None
        LastNodeInList = self.ConvertNode(RootOfTree, LastNodeInList)
#         LastNodeInList is end point
        while(LastNodeInList.left):
            LastNodeInList = LastNodeInList.left
        return LastNodeInList

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(14)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)
    root.right.right.right = TreeNode(18)
    res = s.Convert(root)

    while(res):
        print(res.val)
        res = res.right
