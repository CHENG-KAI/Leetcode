# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        res = []
        res2 = []
        level2 = 0
        while level:
            queue = []
            level2 += 1
            for i in level:
                res.append(i.val)
                if i.right:
                    queue.append(i.right)
                if i.left:
                    queue.append(i.left)
            level = queue
            res = res[::-1] if level2 % 2 == 1 else res
            res2.append(res)
            res = []
        return res2
    
    
    
