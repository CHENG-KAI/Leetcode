def permuteUnique(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        dfs(nums,0,[],res,len(nums))
        return res
def dfs(nums,index,path,res,l):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                    continue
            dfs(nums[:i]+nums[i+1:],i,path+[nums[i]],res,l)
nums = [1,2,3]
permuteUnique(nums)
