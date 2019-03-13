# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res_list = [[root]]
        res = []
        while (res_list):
            eachs = res_list.pop(0)
            next_level = []
            return_val = []
            for each in eachs:
                print(each.val)
                return_val.append(each.val)
                if each.left:
                    next_level.append(each.left)
                if each.right:
                    next_level.append(each.right)
            if next_level != []:
                res_list.append(next_level)
            res.append(return_val)
        return res
