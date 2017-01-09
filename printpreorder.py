class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution(object):
    def printPreorder(self,root):
        if root:
            print root.val
            self.printPreorder(root.left)
            self.printPreorder(root.right)




first = Solution()
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
first.printPreorder(root)
