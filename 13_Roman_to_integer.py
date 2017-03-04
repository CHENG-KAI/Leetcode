class Solution(object):
    def romanToInt(self,s):
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        i = 0
        while i < len(s):
            var1 = dict[s[i]]
            if i+1 >= len(s):
                var2 = 0
            else:
                var2 = dict[s[i+1]]
            if var2 > var1:
                sum = sum + (var2-var1)
                i+=1
            else:
                sum = sum+var1
            i+=1
        return sum
    
