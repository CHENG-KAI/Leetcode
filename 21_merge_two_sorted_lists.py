class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur =cur.next
            else:
                cur.next = l2
                l2 =l2.next
                cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next


l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(6)
l2.next = ListNode(7)
l2.next.next = ListNode(8)

first = Solution()
print first.mergeTwoLists(l1,l2)

                
                
