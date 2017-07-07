def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False 
    i,j = 0,0
    while i < len(s) and j <len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return True if i == len(s) else False
    
    
s = "abec"
t = "ahbgdc"

print isSubsequence(s, t)




def isSubsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)

