class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
       


class Solution(object):
    
    def flatten(self,root):
        prev = []
        self.dfs(root,prev)
        cur = pry = Treenode(-1)
        for i in prev:
            pry.next = Treenode(i)
            pry = pry.next
        return cur.next
        
    def dfs(self, root,prev):
    
        #global variable to remember previous node.
        if not root:
            
        
            return
        if root.val:
            prev.append(root.val)
        else:
            prev.append(None)
        self.dfs(root.left,prev)
        self.dfs(root.right,prev)
        return prev
        


root = Treenode(0)

first = Solution()

#print first.flatten(root)
print first.flatten(root)
