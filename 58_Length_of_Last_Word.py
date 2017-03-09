class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if s == []:
            return 0
        a = len(s)-1
        return len(s[a])
