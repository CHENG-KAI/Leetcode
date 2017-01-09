class Node:
    def __init__(self,val,l,r):
        self.val = val
        self.l = l
        self.r = r 

class Solution(object):
    def isSameTree(self,p,q):

        queue = [(p,q)]
        while queue:
                 a, b = queue.pop()
                 

                 if a == None and b == None:
                     continue
                 elif a and b and a.val == b.val:
                     queue.append([a.l, b.l])
                     queue.append([a.r, b.r])

                 else:
                     return False
        return True


root1 = Node(3,None,None)
root1.l=Node(4,None,None)
root1.r=Node(5,None,None)
root2 = Node(3,None,None)
root2.l=Node(4,None,None)
root2.r=Node(5,None,None)

first = Solution()
print first.isSameTree(root1,root2)
