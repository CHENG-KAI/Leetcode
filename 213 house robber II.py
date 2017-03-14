class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums)
        return max(self.rob_path(nums,2,n-1)+nums[0],self.rob_path(nums,1,n))


    def rob_path(self,nums,start,end):
        x = 0
        y = 0
        for i in range(start,end):
            if (i&1):
                x = max(x+nums[i],y)
        
            else:
                y = max(y+nums[i],x)
        return max(x,y)
        
