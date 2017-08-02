# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        queue = [root]
        level = 0
        
        while queue:
            level+=1
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level






class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth



root = Treenode(2)
root.left = Treenode(3)
root.left.right = Treenode(1)
root.right = Treenode(5)
root.right.right = Treenode(7)
first = Solution()
print first.maxDepth(root)
