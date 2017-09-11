#using dp 
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dp[i+1] += dp[i]
        return max(dp)


#optimize the space
class Solution(object):
    def findLengthOfLCIS(self, nums):
        res1 = 0
        res2 = 1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                res2+=1
            else:
                res1 =  max(res1,res2)
                res2 = 1
        return max(res1,res2)
             
            
