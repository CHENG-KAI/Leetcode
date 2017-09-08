class Solution(object):
    def __init__(self):
        self.ans = float('inf')
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        
        if root:
            self.ary.append(root.val)
            self.findSecondMinimumValue(root.left)
            self.findSecondMinimumValue(root.right)
            #list(set(sorted(self.ary)))
        return -1 if len(sorted(set(self.ary))) == 1 else sorted(set(self.ary))[1]
