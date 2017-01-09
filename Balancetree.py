class Node:
    def __init__(self,x,left,right):
        self.val = x
        self.left =None
        self.right =None

class Solution(object):
    def Balance(self,root):
        return getHight(root)>=0

def getHight(root):
    if not root:
        return 0
    l = getHight(root.left)
    if l == -1:
        return -1
    r = getHight(root.right)
    if r == -1:
        return -1
    if abs(l-r)>1:
        return -1
    else:
        return max(l,r) +1


root = Node(1,None,None)
root.left = Node(2,None,None)
root.left.left = Node(2,None,None)
first = Solution()
print first.Balance(root)



class Node:
    def __init__(self,x,left,right):
        self.val = x
        self.left =None
        self.right =None

class Solution(object):
    def Balance(self,root):
        return self.getHight(root)>=0

    def getHight(self,root):
        if not root:
            return 0
        l = self.getHight(root.left)
        r = self.getHight(root.right)

        if l == -1 or r ==-1 or abs(l-r)>1:
            return -1
        else:
            return max(l,r) +1



root = Node(1,None,None)
root.left = Node(2,None,None)
root.left.left = Node(2,None,None)
first = Solution()
print first.Balance(root)
