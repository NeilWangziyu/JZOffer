# 并查集顾名思义就是有“合并集合”和“查找集合中的元素”两种操作的关于数据结构的一种算法。

# 用集合中的某个元素来代表这个集合，该元素称为集合的代表元。
# 一个集合内的所有元素组织成以代表元为根的树形结构。
# 对于每一个元素 parent[x]指向x在树形结构上的父亲节点。如果x是根节点，则令parent[x] = x。
# 对于查找操作，假设需要确定x所在的的集合，也就是确定集合的代表元。可以沿着parent[x]不断在树形结构中向上移动，直到到达根节点。

# 1、维护无向图的连通性。支持判断两个点是否在同一连通块内，和。
# 2、判断增加一条边是否会产生环：用在求解最小生成树的Kruskal算法里。


# https://blog.csdn.net/ten_sory/article/details/81135422

def union_find(edges):
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])

    node_father = {}
    for node in nodes:
        node_father[node] = node

    for edge in edges:
        if node_father[edge[1]] == edge[1]:
            node_father[edge[1]] = edge[0]
        else:
            node_father[edge[0]] = edge[1]

    print(node_father)

    for node in nodes:
        father = node_father[node]
        print(node)
        while father != node_father[father]:
            father = node_father[father]
        node_father[node] = father

    return len([node_father.keys()]), node_father

if __name__ == "__main__":
    nodes = list(range(0, 10))

    test_edges = [[0, 1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]
    test_edges = [['F', 'H'], ['A', 'C'], ['H', 'A']]

    n, pyq = union_find(test_edges)
    print(n, pyq)

