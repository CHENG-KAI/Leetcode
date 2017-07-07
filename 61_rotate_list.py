class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head,k):
        if not head:
            return None
        l = 1
        cur = head
        while head.next:
            l+=1
            head = head.next
        k %= l
        head.next = cur
        for i in range(l-k-1):
            cur = cur.next
         
        
        last = cur
        cur = cur.next
        last.next = None
        return cur
        
            





head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


first = Solution()
first.rotateRight(head,2)
