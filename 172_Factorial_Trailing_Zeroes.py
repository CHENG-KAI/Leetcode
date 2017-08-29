class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """dp TLE"""
        """ 
        if n ==0:return 0
        dp = [1]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]*i
        string = str(dp[-1])[::-1]
        c = 0
        for i in string:
            if i == "0":
                c+=1
            else:break
        return c
        """
        return 0 if n<5 else self.trailingZeroes(n/5)+n/5
            
