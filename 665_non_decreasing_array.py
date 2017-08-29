class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in xrange(1,len(nums)):
            if cnt>1:
                return False
            if nums[i-1] > nums[i]:
                cnt+=1
                if i==1 or nums[i-2]<=nums[i]: nums[i-1]=nums[i]
                else:nums[i]=nums[i-1]
                
                
        return cnt<=1
