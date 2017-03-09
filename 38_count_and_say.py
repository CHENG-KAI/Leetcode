class Solution(object):
    def cmp(self,s):
        s = str(s)
        temp = str(s[0][0])
        res = []
        for i in xrange(1,len(s)):
            if s[i] in temp:
                temp = temp + s[i] 
                
            else: 
                res.append(temp)
                temp = ""
                temp = temp + s[i]
        res.append(temp)      
        return res

    def countAndSay(self,s):
        if s == 1:
            return "1" 
        elif s >= 2:
            s = self.countAndSay(s-1)
        
        s = str(s)
        a = self.cmp(s)
        q = ""
        for i in xrange(len(a)):
            r = a[i]
            e = r[0]
            q = q + str(len(a[i]))+e

        return q
