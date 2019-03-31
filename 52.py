class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def FindFirstCommonNode(self, head1, head2):
        if not head1:
            return None
        if not head2:
            return None
        help_stack1 = []
        help_stack2 = []
        root1 = head1
        root2 = head2
        while(head1):
            help_stack1.append(head1)
            head1 = head1.next
        while(head2):
            help_stack2.append(head2)
            head2 = head2.next
        prev = None
        while(help_stack1 and help_stack2):
            if help_stack1[-1].val == help_stack2[-1].val:
                prev = help_stack1.pop()
                help_stack2.pop()

            else:
                if prev:
                    return prev.val
                else:
                    return None

        return None

s = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head2 = ListNode(6)
head2.next = ListNode(7)
head2.next.next = head1.next.next.next.next
head2.next.next.next = ListNode(8)
print(s.FindFirstCommonNode(head1, head2))