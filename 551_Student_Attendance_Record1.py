def checkRecord(s):
    t = dict(collections.Counter(s))
    if "A" in s:
        if t["A"] > 1:
            return False
    if "LLL" in s:
            return False
    return True
        

import collections 
s= "PPALLL"
print checkRecord(s)
