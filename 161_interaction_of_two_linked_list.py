class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def getinteraction(self,headA,headB):
        m = self.getsize(headA)
        n = self.getsize(headB)
        
        if m < n:
            return getinteraction(self,headB,headA)
            
        for i in range(m-n):
            headA = headA.next
            
        while headA and headB:
            if headA.val == headB.val:
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return None
    
    
    def getsize(self,head):
        m = 0
        while head:
            head = head.next
            m +=1
        return m 
        
    


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def getinteraction(self,headA,headB):
        
        if headA == None or headB == None:
            return None
    
    
        pa = headA
        pb = headB
    
        while pa is not pb:
            
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa 
        
            
            
        
        
        
        
                
                
   
                
            
            
         
                
            
        
    

    


            
                
        
    
    
    





headA = ListNode(1)
headA.next = ListNode(1)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(1)
headA.next.next.next.next = ListNode(1)
headA.next.next.next.next.next = ListNode(2)
headB = ListNode(1)
headB.next = ListNode(1)
headB.next.next = ListNode(3)
first = Solution()
first.getinteraction(headA,headB)
    
    
    
    
    
    
    



