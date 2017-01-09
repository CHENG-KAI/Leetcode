class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
	def rightSideView(self,root):
		res = []
		self.helper(root,0,res)
		return res
	def helper(self,root,level,res):
		if not root:
			return
		if level >= len(res):
			res.append(root.val)
		self.helper(root,right,level+1,res)
		self.helper(root,left,level+1,res)
