# bfs solution  
class Treenode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:  
    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            count = len(queue)
            level = []
            for i in range(count):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0,level)
        return res
        
root = Treenode(2)
root.left = Treenode(3)
root.left.right = Treenode(1)
root.right = Treenode(5)
root.right.right = Treenode(7)
first = Solution()
print first.levelOrderBottom(root)
