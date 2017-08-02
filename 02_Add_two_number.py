#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = rst = ListNode(0)
        carry = sum = 0
        while l1 or l2 or carry > 0:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
                
            if l2!= None:
                sum +=l2.val
                l2 = l2.next
            sum += carry
            list.next = ListNode(sum%10)
            carry = sum/10
            list = list.next
        return rst.next
       
            

            
            
            
            

first = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)   
l1.next.next = ListNode(3) 
l2 = ListNode(5)
l2.next = ListNode(6)   
l2.next.next = ListNode(4)
print first.addTwoNumbers(l1,l2)






#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0);
        cur = result;
        while l1 or l2:
            cur.val += self.addnodes(l1,l2)
            if cur.val >= 10:
                cur.val-=10
                cur.next = ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result
                
            
            
            
        
        
    def addnodes(self,n1,n2):
        if not n1 and n2:
            return None
        if not n1:
            return n2
        if not n2:
            return n1
        return n1.val + n2.val
    
            
                
        
        
        
            
        
            
            
            
            
            

first = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)   
l1.next.next = ListNode(3) 
l2 = ListNode(5)
l2.next = ListNode(6)   
l2.next.next = ListNode(4)
print first.addTwoNumbers(l1,l2)        
                
                
                

                
                
                
