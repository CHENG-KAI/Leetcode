class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def isPalindrome(self, head):
        rev = ""
        pov = ""
        while head:
            rev = head.val + rev
            pov = pov + head.val
            head = head.next
            
        return rev == pov
        
        
        
head = ListNode("s")
head.next = ListNode("i")
head.next.next = ListNode("l")
head.next.next.next = ListNode("i")
head.next.next.next.next = ListNode("s")


first = Solution()
first.isPalindrome(head)
