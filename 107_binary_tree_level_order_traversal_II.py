class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque  
class Solution(object):
    def maxDepth(self,root):
        if not root:
            return None
        
        level = [root]
        res = []
        res2 = []
        while level:
            queue = []
            for i in level:
                res.append(i.val)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)     
            level = queue
            res2.append(res)
            res = []
        return res2[::-1]


root = Treenode(3)
root.left = Treenode(9)
#root.left.right = Treenode(1)
root.right = Treenode(20)
root.right.left = Treenode(15)
root.right.right = Treenode(7)
first = Solution()
print first.maxDepth(root)
            
            
