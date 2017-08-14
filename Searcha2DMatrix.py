class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import bisect
        
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        
        x = [row[-1] for row in matrix]
        r = bisect.bisect_left(x, target)
        if r == m: return False
        row = matrix[r]
        c = bisect.bisect_left(row, target)
        return target == row[c]