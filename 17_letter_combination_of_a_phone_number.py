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




class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.dic = {"1":"",
               "2":["a","b","c"],
               "3":["d","e","f"],
               "4":["g","h","i"],
               "5":["j","k","l"],
               "6":["m","n","o"],
               "7":["p","q","r","s"],
               "8":["t","u","v"],
               "9":["w","x","y","z"],
        }
        res = []
        temp = []
        self.dfs(digits,0,temp,res)
        return res
    def dfs(self,digits,index,temp,res):
        if len(digits) == len(temp):
            res.append("".join([x for x in temp]))
            return 
        for i in self.dic[digits[index]]:
            temp.append(i)
            self.dfs(digits,index+1,temp,res)
            temp.pop()
            
first = Solution()
first.letterCombinations("23")

