class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
class Solution(object):
    def invertbinary(self,root):
        if root == None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertbinary(root.left)
        self.invertbinary(root.right)
        return root 

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
first = Solution()
first.invertbinary(root)





