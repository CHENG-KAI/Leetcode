class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == ''.join(reversed(s)):return True
        j = len(s)-1
        i = 0
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            if s[i] != s[j]:
                # take abca as example
                # s[i:j:] is b
                # s[i+1:j+!:] is c
                return s[i:j:][::-1] == s[i:j:] or s[i+1:j+1:][::-1] == s[i+1:j+1:]
                #if s[i:j:][::-1] == s[i:j:] or s[i+1:j+1:][::-1] == s[i+1:j+1:] :return True
                #else:return False
        return True
            
            
