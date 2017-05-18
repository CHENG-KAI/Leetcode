class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self,head,val):
        if head == None:
            return None
        
        prev = ListNode(0)
        prev.next = head
        
        while head:
            if head.val != val:
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = head.next
        return prev.next
                
        
    
    
    
    
    



first = Solution()
head = ListNode(1)
head.next = ListNode(2)   
head.next.next = ListNode(3) 
head.next.next.next = ListNode(4) 
print first.removeElements(head,3)







class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        head, head.next = ListNode(0), head
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else: p = p.next
        return head.next
            
        
            
                






head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

first = Solution()
first.removeElements(head,4)

