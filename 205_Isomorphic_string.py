class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find,s) == map(t.find,t)

"""
>> s = "add"
>> map(s.find,s)
>>[0,1,1]

>> s = "add"
>> map(t.find,t)
>>[0,1,1]

"""



"""
hash table solution

"""
def halfIsom(s, t):
    res = {}
    for i in xrange(len(s)):
        if s[i] not in res:
            res[s[i]] = t[i]
        elif res[s[i]] != t[i]:
            return False
    return True
s = "rssas"
t = "taabl"    
