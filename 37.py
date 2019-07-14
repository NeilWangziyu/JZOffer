class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 序列化二叉树and反序列化

class Codec:
    # 利用层序遍历进行序列化
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "n"
        s = ""
        stack = [root]
        while (stack):
            root = stack.pop(0)
            if root:
                s += str(root.val)
                stack.append(root.left)
                stack.append(root.right)
            else:
                s += 'n'
            s += ' '
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        tree = data.split()

        if tree[0] == 'n':
            return None

        queue = []
        root = TreeNode(int(tree[0]))
        queue.append(root)
        i = 1
        while (queue):
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != 'n' else None
            cur.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != 'n' else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root



class Codec2:
    # as JZ offer，利用前序遍历
    # 但是实现起来其实比较复杂，从另一个角度来说，其空间复杂度比较低
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def serialize_core(root):
            str = ""
            if not root:
                str += '$'
                str += " "
                return
            str += str(root.val)
            str += " "
            return str + serialize_core(root.left) +  serialize_core(root.right)


        if not root:
            return "$ "
        return serialize_core(root)





    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        print(data)
        data = data.split(" ")


