class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        res = 0
        start, end = arrays[0][0],arrays[0][-1]
        for row in arrays[1:]:
            res = max(res,abs(row[-1]-start))
            res = max(res,abs(row[0]-end))
            start = min(start,row[0])
            end = max(end,row[-1])
        return res
