class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        a = []
        self.dic,res = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi',
        '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'} , [""]
        for x in digits:
            newresult = []
            for char in self.dic[x]:
                for string in res:
                    newresult.append(string+char)
            res = newresult
        return res
        
        
            


first = Solution()
first.letterCombinations("234")




