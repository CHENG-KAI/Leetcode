class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = int('-'+str(x)[:0:-1]) 
            
        if 2147483647 > x > -2147483647:
            return x
        else:
            return 0


     def reverse_v2(self, x):
          if x >= 0:
            x = int(str(x)[::-1])
          else:
            x = int('-'+str(x)[:0:-1])
          return x if 2147483647 > x > -2147483647 else 0
         
