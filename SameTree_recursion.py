class Node:
    def __init__(self,val,left,right):
        self.val =val
        self.left = left
        self.right = right


def isSameTree(p,q):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        return False


#http://stackoverflow.com/questions/39436570/lowest-common-ancestor-how-to-build-the-tree-from-command-line-input
#https://www.youtube.com/watch?v=as1f6PJmbAE&list=PLvHc59peqCbMehStbdtfDAFArkAOb3Id6
root1 = Node(3,None,None)
root1.left=Node(2,None,None)
root1.right=Node(5,None,None)
root2 = Node(3,None,None)
root2.left=Node(2,None,None)
root2.right=Node(4,None,None)
print isSameTree(root1,root2)


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        solution = self.isSameTree(p.left, q.left)
        solution = solution and self.isSameTree(p.right, q.right)
        return solution


#http://jelices.blogspot.com/2014/06/leetcode-python-same-tree.html

    
