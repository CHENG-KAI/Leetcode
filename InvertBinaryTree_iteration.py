class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self,root):
        stack = [root]
        #res = [] 
        while stack:
            node = stack.pop()
            if node:
                node.left , node.right = node.right , node.left
                stack.append(node.left)
                stack.append(node.right)
        #res = [root.val,root.left.val,root.right.val]
        #print res
        return root 

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
first = Solution()
first.invertTree(root)
