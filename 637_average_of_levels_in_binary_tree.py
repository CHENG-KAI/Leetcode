# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
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
            s = sum(res)/float(len(res))
            res2.append(s)
            s = 0
            res = []
            
        return res2
                
                
