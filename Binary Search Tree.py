class Node:
    def __init__(self,val,key,l,r):
        self.l=l
        self.r=r
        self.val=val
        self.key=key


def search(value,p):
    if(p.val== value):
         print ("You bought a", p.key)
         return
    else:
        if(p.val<value):
            search(value,p.r)
        if(p.val>value):
            search(value,p.l)
            
            

root = Node(3,"Chips",None,None)
root.l = Node(1,"Raspberry",None,None)
root.l.r = Node(2,"Mac",None,None)
root.r= Node(2,"Sam",None,None)
root.r.l= Node(2,"TV",None,None)
root.r.r= Node(2,"Chicken",None,None)

search(2,root)


#https://www.youtube.com/watch?v=0wfpgEPN0NQ&t=42s
