class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "1":
                    ans+=1
                    self.dfs(grid,i,j,m,n)
        return ans
    def dfs(self,grid,i,j,m,n):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid,i+1,j,m,n)
        self.dfs(grid,i-1,j,m,n)
        self.dfs(grid,i,j+1,m,n)   
        self.dfs(grid,i,j-1,m,n)   
                    
