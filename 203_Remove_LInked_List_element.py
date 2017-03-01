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
