class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
class Solution(object):
    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print root.val
            self.printInorder(root.right)
     

first = Solution()
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
#root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
#root.right.right = Node(7)
first.printInorder(root)
