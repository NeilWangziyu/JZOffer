class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        finished_head = None
        while(head):
            prev = head
            head = head.next
            prev.next = finished_head
            finished_head = prev
        return finished_head



if __name__ == "__main__":
    pass