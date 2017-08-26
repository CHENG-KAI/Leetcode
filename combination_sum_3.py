class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = []
    
        self.dfs(range(1,10),0,[],res,k,n)
        return res
    def dfs(self,nums,index,path,res,k,n):
        if sum(path) >n:
            return
    
        if len(path) == k and sum(path) == n:
            res.append(path)
            return
        #if len(path) + len(nums[index:])<k:return
        for i in xrange(index,len(nums)):
            self.dfs(nums,i+1,path+[nums[i]],res,k,n)
