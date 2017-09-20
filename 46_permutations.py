class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
    
        self.dfs(nums,0,[],res,len(nums))
        return res
    def dfs(self,nums,index,path,res,l):
    
    #if len(path) <= len(nums):
        if len(path) == len(nums):
            res.append(path)
        #return
    
        for i in xrange(len(nums)):
            if nums[i] in path:
                continue
            self.dfs(nums,i,path+[nums[i]],res,l)


"""
               []
             /  |  \
            1   2   3
          / | \
        11  12 13


"""
