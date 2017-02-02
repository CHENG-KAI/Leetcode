class Node:
    def __init__(self,val):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelorder(self,root):
        rst = {}
        tem = []
        self.helper(root,0,rst)
        for i in rst:
            tem.append(rst[i])
        return tem 
            

        
    def helper(self,root,level,rst):
        if root == None:
            return
        for level not in rst:
            rst[level] = []
        rst[level].append(root.val)
        self.helper(root.left,level+1,rst)
        self.helper(toor.right,level+1,rst)

root = Node(1)
root.left = Node(2)
root.right = Node(3)



