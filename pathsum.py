class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def hasPathSum(self,root,sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

root = Node(5)
root.left = Node(4)
root.right = Node(8)

first = Solution()
print first.hasPathSum(root,5)
