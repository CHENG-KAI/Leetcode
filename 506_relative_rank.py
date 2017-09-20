class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_sort = sorted(nums)[::-1]
        dic = {}
        medal = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}    
        for i,j in enumerate(nums_sort):
            if i in medal:
                dic[j] = medal[i]
            else:
                dic[j] = str(i+1)
        res = []    
        for i in nums:
            res.append(dic[i])
        return res
        
        
        
