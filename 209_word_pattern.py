class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        return map(pattern.index,pattern) == map(str.index,str)


def wordPattern(pattern, str):
    if len(pattern) != len(str.split()):
        return False
    d1, d2 = {}, {}
    for p, r in zip(pattern, str.split()):
        if p in d1:
            if d1[p] != r:
                return False
        d1[p] = r
        
        if r in d2:
            if d2[r] != p:
                return False
        d2[r] = p
        
    return True
    
print wordPattern("abba","dog dog dog dog")
