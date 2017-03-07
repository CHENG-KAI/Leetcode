class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s.lower())
        b = []
        for i in s:
            if i.isalnum():
                a.append(i)
        return a == a[::-1]
