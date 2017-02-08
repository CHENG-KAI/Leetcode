class Solution(object):
    def searchMatrix(self,matrix,target):
        
    #searchMatrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
        if not matrix:
            return False
        
        m = len(matrix[0])
        n = len(matrix)

        l, r = 0, m-1 
        while l <= n-1 and r >= 0:
            if target == matrix[l][r]:
                return True
            elif target > matrix[l][r]:
                l +=1
            elif target < matrix[l][r]:
                r -=1
        return False


#Stair search method
#if the target is greater than top-right element => go down
#if the target is greater than top-right element => go left
#Time capacity is O(n)





class Solution(object):
    def searchMatrix(self,matrix,target):
        if not matrix:
            return False
       
        n = len(matrix)
        m = len(matrix[0])
       
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == target:
                    return True
        return False

#Brute force method
#Time capacity is O(N2)



class Solution(object):
    def searchMatrix(self,matrix,target):
        
    #searchMatrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
        import bisect 
        if not matrix:return False
        m = len(matrix[0])
        if m == 0:return False
        n = len(matrix)
        if n == 0:return False
        row = [] 
        for i in xrange(n):
            row.append(matrix[i][m-1])
    
        r = bisect.bisect_left(row,target)
        if r == n: return False
        o = bisect.bisect_left(matrix[r],target)
        if matrix[r][o] == target:
            return True
        else:return False

#apply bisect algorithm 



