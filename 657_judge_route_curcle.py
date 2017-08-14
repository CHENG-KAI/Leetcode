class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        pos = 0
        for i in moves:
            if i == "R" or i == "U" :
                pos+=1
            else: pos-=1
        if pos == 0:
            return True
        else:return False
            
            
