class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self,preorder,inorder):
        if len(inorder) > 0:
            mid = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[mid])
            print root.val
            root.left = self.buildTree(preorder, inorder[:mid])
            root.right = self.buildTree(preorder,inorder[mid+1:])
            return root



first = Solution()
preorder = [1,2,3]
inorder  = [2,1,3]
first.buildTree(preorder,inorder)
