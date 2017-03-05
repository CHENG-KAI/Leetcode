class Solution(object):
    def reverseVowels(self,s):
        s = list(s)
        j = len(s)-1
        vowel = "aeiouAEIOU"
        i = 0
        while i < j:
            while s[i] not in vowel and i < j:
                i+=1
            while s[j] not in vowel and i < j:
                j-=1
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return "".join(s)


    def reverseVowels2(self,s):
        s = list(s)
        j = len(s)-1
        vowel = "aeiouAEIOU"
        i = 0
        while i < J:
            if s[i] in vowel and s[j] in vowel:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            if s[i] not in vowel:
                i+=1
            if s[j] not in vowel:
                j-=1
        return "".join(s)
                
                
