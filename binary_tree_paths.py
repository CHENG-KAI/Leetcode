class Solution(object):
    def binaryTreePaths(self,root):
        if root == None:
            return []
        rst = []
        self.helper(root,str(root.val),rst)
        return rst

        

    def helper(self,root,path,rst):
        if root.left:
            self.helper(root.left,path + "->" + str(root.left.val), rst)
        if root.right:
            self.helper(root.right,path + "->" + str(root.right.val), rst)
        if root.left == None and root.right == None:
            rst.append(path)

