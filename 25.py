class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergetwolists(self, l1, l2):  # 首先合并两个链表的
        l3 = ListNode(0)  # 空链表
        cur = l3
        while (l1 != None) & (l2 != None):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        l3 = l3.next
        return l3