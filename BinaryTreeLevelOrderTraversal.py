class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def levelorder(self,root):
        tem = []
        self.recur(root,tem)
        return tem

    def recur(self,root,tem):
        if root == None:
            tem.append("#")
            return
        tem.append(root.val)
        self.recur(root.left,tem)
        self.recur(root.right,tem)
        
root = Node(3)
root.left = Node(9)
root.left.right = Node(7)
root.right = Node(20)
first = Solution()
print first.levelorder(root)

