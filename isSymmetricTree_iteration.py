class Node:
    def __init__(self,val,left,right):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def isSymmetric(self,root):
        if root == None:
           return True
        stack = [(root.left,root.right)]
        while stack:
            l,r = stack.pop()
            if l == None and r == None:
                continue
            elif l and r and l.val == r.val:
                stack.append((l.left,r.right))
                stack.append((l.right,r.left))
            else:
                return False
        return True


root = Node(1,None,None)
root.left = Node(2,None,None)
root.right = Node(2,None,None)
root.left.left = Node(3,None,None)
root.left.right= Node(4,None,None)
root.right.left= Node(4,None,None)
root.right.right= Node(3,None,None)

first = Solution()
print first.isSymmetric(root)
