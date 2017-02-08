def searchmatrix():
    
    matrix = [[2,3]]
    m = len(matrix[0])
    n = len(matrix)
    a,b,c,d = 0,n,m,0
    dir = 0 
    o = []
    
    if not matrix:
        return []
    
    while b > a and c > d:
        
        if dir == 0:
           for i in xrange(d,c):
               o.append(matrix[a][i])
           a+=1
           dir = 1
        elif dir == 1:
            for i in xrange(a,b):
                o.append(matrix[i][c-1])
            c-=1
            dir = 2
        elif dir == 2:
            for i in reversed(xrange(d,c)):
                o.append(matrix[b-1][i])
            b-=1
            dir = 3
        elif dir == 3:
            for i in reversed(xrange(a,b)):
                o.append(matrix[i][d])
            d+=1
            dir = 0
    return o
                

print searchmatrix()
            


class Solution(object):
    def spiralOrder(self, matrix):
        
        
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        if not matrix:
            return []
        
        
        m = len(matrix[0])
        n = len(matrix)
        a,b,c,d = 0,n,m,0
        dir = 0 
        o = []
       
    
        while b > a and c > d:
            if dir == 0:
                for i in xrange(d,c):
                    o.append(matrix[a][i])
                a+=1
                dir = 1
            elif dir == 1:
                for i in xrange(a,b):
                    o.append(matrix[i][c-1])
                c-=1
                dir = 2
            elif dir == 2:
                for i in reversed(xrange(d,c)):
                    o.append(matrix[b-1][i])
                b-=1
                dir = 3
            elif dir == 3:
                for i in reversed(xrange(a,b)):
                    o.append(matrix[i][d])
                d+=1
                dir = 0
        return o
        

#https://www.youtube.com/watch?v=siKFOI8PNKM 


            
    

