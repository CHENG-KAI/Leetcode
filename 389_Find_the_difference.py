def findTheDifference(s, t):
    return list((collections.Counter(t) - collections.Counter(s)))[0]
    
            
    
def findTheDifference(s, t):
    for ch in t:
        if (s+t).count(ch)%2:
            return ch; 
    
    
    
import collections
s = "a"
t = "aa"
findTheDifference(s, t)
