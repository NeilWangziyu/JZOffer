# import sys
#
#
# class TreeNode():
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# def search(root, val):
#     if not root:
#         return None
#     else:
#         if root.val == val:
#             return root
#         else:
#             left_result = search(root.left, val)
#             right_result = search(root.right, val)
#
#             if left_result:
#                 return left_result
#             elif right_result:
#                 return right_result
#             else:
#                 return None
#
#
#
# def get_height(root, count):
#     if not root:
#         return count
#     else:
#         return max(get_height(root.left, count + 1), get_height(root.right, count + 1))
#
#
# n = int(sys.stdin.readline().strip())
# if n == 0:
#     print(0)
# ans = 0
# root = None
# wait_for_next = []
# for line in sys.stdin:
#     values = sys.stdin.readline().strip()
#     if not values:
#         break
#     values = values.split()
#     father = int(values[0])
#     son = int(values[1])
#     if not root:
#         root = TreeNode(father)
#         if son >= root.val:
#             root.right = TreeNode(son)
#         else:
#             root.left = TreeNode(son)
#     else:
#         checked_node = search(root, father)
#         if not checked_node:
#             wait_for_next.append([father, son])
#         else:
#             if son >= father:
#                 checked_node.right = TreeNode(son)
#             else:
#                 checked_node.left = TreeNode(son)
# print(wait_for_next)
# if wait_for_next:
#     for each in wait_for_next:
#         father = each[0]
#         son = each[1]
#         checked_node = search(root, father)
#         if checked_node:
#             if son >= father:
#                 checked_node.right = TreeNode(son)
#             else:
#                 checked_node.left = TreeNode(son)
#
# ans = get_height(root, 0)
# print(ans)
#
# check_tem = TreeNode(0)
# check_tem.left = TreeNode(1)
# check_tem.right = TreeNode(2)
# check_tem.left.left = TreeNode(-1)
# print(get_height(check_tem, 0))
#
#
#
#
#
#
#
# import sys
# n = int(sys.stdin.readline().strip())
# if n == 0:
#     print(0)
# graph = []
# dict_tem = {}
#
# for line in sys.stdin:
#     values = sys.stdin.readline().strip()
#     if not values:
#         break
#     values = values.split()
#     father = int(values[0])
#     son = int(values[1])
#
#     graph.append([father, son])
#     if father not in dict_tem:
#         dict_tem[father] = 1
#         dict_tem[son] = 2
#     else:
#         dict_tem[son] = dict_tem[father] + 1
#
# # print(graph)
# # print(dict_tem)
# ans = 0
# for each in dict_tem.keys():
#     if dict_tem[each] > ans:
#         ans = dict_tem[each]
# print(ans)

# 树的高度
# ——————————————————————————————————————————————
def height(X, node):
    l = len(X[node])
    r = 0
    for i in range(l):
        r = max(height(X, X[node][i]), r)
    return 1 + r


def main():
    n = int(input())
    X = [[] for _ in range(n)]
    for i in range(n - 1):
        x, y = map(int, input().split())
        if (len(X[x]) < 2):
            X[x].append(y)

    print(height(X, 0))

main()


# ——————————————————————————————————————————————
def havechild(node_list, td):
    for node in node_list:
        if node in td:
            if len(td[node]) > 0:
                return True
    return False


def height_tree(m):
    tree_dict = {}
    for i in m:
        if i[0] not in tree_dict:
            tree_dict[i[0]] = [i[1]]
        else:
            if len(tree_dict[i[0]]) < 2:
                tree_dict[i[0]].append(i[1])
    tree_stack = [[0]]
    while havechild(tree_stack[-1], tree_dict):
        new_layer = []
        for node in tree_stack[-1]:
            if node in tree_dict:
                new_layer.extend(tree_dict[node])
        tree_stack.append(new_layer)
    return len(tree_stack)


def main():
    num_node = int(input())
    tree = []
    for _ in range(num_node - 1):
        line = input().strip().split()
        tree.append(
            list(map(int, line))
        )
    tree_h = height_tree(tree)
    print(tree_h)


main()
map