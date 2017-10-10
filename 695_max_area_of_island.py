class Solution(object):
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.area = 0
        maxarea = -1 
        m = len(grid)
        if m == 0:return 0
        n = len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    area = 0
                    self.dfs(grid,i,j,m,n)
                if self.area > maxarea: maxarea = self.area
                self.area = 0
        return maxarea 
    def dfs(self,grid,i,j,m,n):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.area +=1
        self.dfs(grid,i+1,j,m,n)
        self.dfs(grid,i-1,j,m,n)
        self.dfs(grid,i,j+1,m,n)   
        self.dfs(grid,i,j-1,m,n) 
            
                
                
                
                
                
        
        
        
