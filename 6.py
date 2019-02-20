class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def PrintListReversingly(self, listNode):
        if not listNode:
            return []
        res = []
        while(listNode):
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res
