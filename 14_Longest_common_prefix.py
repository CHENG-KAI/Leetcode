class Solution(object):
    def longestCommonPrefix(self,strs):
        s = zip(*strs)
        res = ""
        for i in xrange(len(s)):
            if len(set(s[i])) > 1:
                break
            res +=s[i][0]
        return res  
