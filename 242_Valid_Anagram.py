class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       
        return sorted(s) == sorted(t)



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        import collections
        return collections.Counter(s) == collections.Counter(t)
        
        
        
