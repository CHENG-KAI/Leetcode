class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        return haystack.find(needle)





"""
s = "abcde"
a = "de"
print s[0:2:]
print s[1:3:]
print s[2:4:]
print s[3:5:]
"""
def long(haystack,needle):
    for i in xrange(len(haystack)+1):
        if haystack[i:i+len(needle):] == needle:
            return i
    return -1
    
haystack = ""
needle = ""
print long(haystack,needle)
