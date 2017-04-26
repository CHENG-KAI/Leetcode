class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = collections.Counter(s)
        res , single = 0, 0
        for i in str.values():
            if i % 2 == 0:
                res += i
            else:
                single = 1
                res += i/2*2
        return res + single


