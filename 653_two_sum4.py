# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
    
        level = [root]
        
        array = [root.val]
        res = 0
        while level:
            queue = []
            for i in level:
                if i.left:
                    queue.append(i.left)
                    array.append(i.left.val)
                if i.right:
                    queue.append(i.right)
                    array.append(i.right.val)
            level = queue
        
        array.sort()
        
        i,j = 0,len(array)-1
        while i < j:
            if array[i]+array[j] == k:return True
            elif array[i]+array[j] < k:i+=1
            else:j-=1
        return False
    
            
            
