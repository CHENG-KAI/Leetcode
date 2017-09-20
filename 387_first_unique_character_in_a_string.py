class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        from collections import Counter
        res = dict(Counter(s))
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
            
        return -1
