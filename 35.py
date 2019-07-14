# not finished yet

class ComplexListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.sibing = None

def buildCLN(list_v):
    if not list_v:
        return
    res = ComplexListNode(list_v[0])
    head = res
    for each in list_v[1:]:
        head.next = ComplexListNode(each)
        head = head.next

    return res




class Solution():
    def CopyComplexListNode(self, head):

        def cloneList(head):
            if not head:
                return head
            first = head
            while(head):
                old_head_next = head.next
                head.next = ComplexListNode(head.val)
                head = head.next
                head.next = old_head_next
                head = head.next
            return first

        def reconnectList(head):
            if not head:
                return head
            res = head
            while(head):
                head_connect = head.sibing
                head.next.sibing = head_connect
                head = head.next.next
            return res

        def separate(head):
            if not head:
                return head
            next_res = head.next
            while(head):
                head = head.next.next
                next_res.next = head.next
            return next_res

        head = cloneList(head)
        head = reconnectList(head)
        return separate(head)

if __name__ == "__main__":
    s = Solution()
    CLN = buildCLN(['A', 'B', 'C', 'D', 'E'])
    copy_list = s.CopyComplexListNode(CLN)

    while(copy_list):
     print(copy_list.val)
     print(copy_list.sibing.val)
    copy_list = copy_list.next



