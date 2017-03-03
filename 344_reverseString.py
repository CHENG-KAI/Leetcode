class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))
    def reverseString2(self,s):
        t = ""
        q = list(s)
        r = len(q)
        for i in xrange(r-1,-1,-1):
            t = t + q[i]
        return t 
    def reverseString3(self,s):
        return s[::-1]
        
