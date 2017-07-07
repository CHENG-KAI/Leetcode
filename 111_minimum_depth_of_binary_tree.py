class Treenode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:  
    def minDepth(self, root):
        if root == None:
            return 0
        queue = []
        queue.append(root)
        
        level = 0
        while queue:
            size = len(queue)
            level +=1
            for i in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                   
        return level
        
        
root = Treenode(2)
root.left = Treenode(3)
root.right = Treenode(5)
first = Solution()
first.minDepth(root)
