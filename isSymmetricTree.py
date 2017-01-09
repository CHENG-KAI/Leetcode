class Node:
    def __init__(self,val,left,right):
        self.val=val
        self.left=None
        self.right=None


class Solution(object):

   def helper(self,l,r):
        if l == None and r == None:
            return True
        elif l and r and l.val == r.val:
            return self.helper(l.left,r.right) and self.helper(l.right,r.left)
        else:
            return False
    
   def isSymmetric(self,root):
        if root == None:
            return True
        return self.helper(root.left,root.right)


root = Node(3,None,None)
root.left = Node(2,None,None)
root.right = Node(2,None,None)
root.left.left = Node(3,None,None)
root.left.right = Node(4,None,None)
root.right.left = Node(4,None,None)
root.right.right = Node(3,None,None)
first = Solution()
print first.isSymmetric(root)






                
