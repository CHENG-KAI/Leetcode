class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != fast:
            fast = fast.next
            head = head.next
        return head               






head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next




first = Solution()
first.detectCycle(head,4)
