class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        
        if root == None:
            return []
        
        level = [root]
        res = []
        res2 = []
        while level:
            queue = []
            for i in level:
                res2.append(i.val)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            res.append(res2)
            res2 = []
            level = queue
        return res
                    
root = Treenode(2)
root.left = Treenode(3)
root.left.right = Treenode(1)
root.right = Treenode(5)
root.right.right = Treenode(7)
first = Solution()
print first.levelOrder(root)                   
                
    
    
