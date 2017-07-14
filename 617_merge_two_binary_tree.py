class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        

class Solution(object):
 
    def mergeTrees(self,t1,t2):  
        if not t1 and not t2: 
            return None    
        if not t1 and t2: 
            result = TreeNode(t2.val) 
            result.left = t2.left 
            result.right = t2.right
        if t1 and not t2: 
            result = TreeNode(t1.val) 
            result.left = t1.left 
            result.right = t1.right
        if t1 and t2: 
            result = TreeNode(t1.val+t2.val) 
            result.left = self.mergeTrees(t1.left,t2.left) 
            result.right = self.mergeTrees(t1.right,t2.right)   
        return result  
        
        
t1 = TreeNode(1) 
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2) 
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right= TreeNode(7)


first = Solution()
print first.mergeTrees(t1,t2)
