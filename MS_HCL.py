# 面了一道第k大的数，一道扑克牌的dp题，一道bfs遍历二叉树

def KthNumber(nums, k):
    if not nums:
        return None
    if k > len(nums):
        return None

    init = nums[0]
    less = []
    more = []
    for each in nums[1:]:
        if each <= init:
            less.append(each)
        else:
            more.append(each)
    if len(more) == k - 1:
        return init
    else:
        if len(more) > k - 1:
            return KthNumber(more, k)
        else:
            return KthNumber(less, k - len(more) - 1)

def bfs_tree(root):
    res = []
    if not root:
        return res
    this_level = [root]
    while(True):
        next_level = []
        for each in this_level:
            res.append(each.val)
            if each.left:
                next_level.append(each.left)
            if each.right:
                next_level.append(each.right)
        if not next_level:
            break
        else:
            this_level = next_level
    return res


 #    有一个整型数组A，代表数值不同的纸牌排成一条线。....
 # * 动态规划
 # * 规定:
 # * (1)玩家a先拿，玩家B后拿.
 # * (2)每个玩家每次只能拿走最左或最右的纸牌.
 # * (3)玩家a和玩家b都绝顶聪明，他们总会采用最优策略。
 # * (4)请返回最后获胜者的分数
 # *
 # * 关于本题一个比较重要的思想:就是code中的第二层for循环里面的a[i][j]和b[i][j]的表达式是怎么得来的.解释如下:
 # * (11)对于选手a,在纸牌范围为[i...j]时,a[i][j]如何表达?
 # *    如果选择A[i],则依赖于选手b的下一次在纸牌范围为[i+1...j]时,a尽量获取本次取牌的最大值且保证b获取下次取牌的尽量较小的值;
 # *    如果选择A[j],则依赖于选手b的下一次在纸牌范围为[i...j-1]时,a尽量获取本次取牌的最大值且保证b获取下次取牌的尽量较小的值.
 # * (22)对于选手b,在纸牌范围为[i...j]时,b[i][j]如何表达?
 # *    作为后手,因为a是足够聪明的,所以b的取值已经被a限制了,b只能取a在[i...j]取完牌后,在a下次取牌前,取出a可以在下次取牌时两种选择状态中值最小的那个,因为a要获得较大的那个嘛
 # *    如果a选择了A[i],那么b只能在纸牌范围为[i+1...j]中选择;
 # *    如果a选择了A[j],那么b只能在纸牌范围为[i...j-1]中选择.

def cardGame(nums):
    a = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    b = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        a[i][i] = nums[i]
        for j in range(i-1, -1, -1):
            # j比i小
            a[j][i] = max(nums[j]+b[j+1][i], nums[i]+b[j][i-1])
            b[j][i] = min(a[j+1][i], a[j][i-1])
    print(a, b)
    return max(a[0][-1], b[0][-1])

print(cardGame([1, 2, 100,4]))



# 题目：随机抽取扑克牌中的5张牌，判断是不是顺子，即这5张牌是不是连续的。其中A看成1，J看成11，Q看成12，K看成13，大小王可以看成任何需要的数字。
# JZoffer 61



# 给你偶数张牌，每次打出相邻两张牌，计分只计左边那张牌的点数，求最佳出牌顺序和分数
# ？？ how to do it

