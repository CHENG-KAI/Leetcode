class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self, head):
        
        
        if head == None and head.next == None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
                
            
            
         
                
            
        
    

    


            
                
        
    
    
    





head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
first = Solution()
first.reverseList(head)
