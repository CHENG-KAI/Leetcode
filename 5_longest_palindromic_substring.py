class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in xrange(len(s)):
            odd = self.therange(i,i,s)
            if len(odd) > len(res):
                res = odd
        
            even = self.therange(i,i+1,s)
            if len(even) > len(res):
                res = even
        return res
    
    def therange(self,l,r,s):
        while l>=0 and r<len(s) and s[r] == s[l]:
            l-=1
            r+=1
        return s[l+1:r]
