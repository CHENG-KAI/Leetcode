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
