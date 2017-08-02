# bfs solution  
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




#DFS solution
#time complexity is O(n)
#space complexity is Olog(n)
class Treenode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        else: 
            return min(self.minDepth(root.left),self.minDepth(root.right))+1

root = Treenode(2)
root.left = Treenode(3)
root.right = Treenode(5)
first = Solution()
first.minDepth(root)





# bfs solution  
class Treenode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:  
    def minDepth(self, root):
        if(not root):
            return 0
        queue = [root]
        level = 1
        while(queue):
            count = len(queue)
            for i in range(0, count):
                node = queue.pop(0)
                if(not node.left and not node.right):
                    return level
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            level += 1
        
        
root = Treenode(2)
root.left = Treenode(3)
root.left.right = Treenode(1)
root.right = Treenode(5)
root.right.right = Treenode(7)
first = Solution()
first.minDepth(root)


