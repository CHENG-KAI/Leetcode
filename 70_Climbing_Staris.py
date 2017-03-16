class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
    
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return max(dp)
        
