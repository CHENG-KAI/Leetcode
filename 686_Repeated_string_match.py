class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
    
        max_repeat_time = (len(B)/len(A))+3
        
        for i in range(1,max_repeat_time):
            if len(A*i) >= len(B):
                if  B in (A*i):
                    return i
        return -1
      
