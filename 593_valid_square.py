class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 == p3 == p4:return False
        def getDistance(x,y):
            return ((x[0]-y[0])**2 + (x[1]-y[1])**2)
        Dist =[getDistance(p1,p2),getDistance(p2,p3),getDistance(p3,p4),getDistance(p1,p4),getDistance(p2,p4),getDistance(p1,p3)]
        Dist.sort()
        if Dist[0] == Dist[1] == Dist[2] == Dist[3]:
            if Dist[4] == Dist[5]:
                return True
        return False
                    
            
        
        
