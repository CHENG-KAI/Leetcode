class Solution(object):
    def cal_len(self,grid):
        
        res = 0
        for i in grid:
            row = 0
            for j in range(len(i)):
                if j != len(i)-1 and i[j] == 1 and i[j+1] == 1:
                    row+=1
            res += row  
        return res
        
    def pre(self,grid):
        ant = []
        for i in grid:
            for j in i:
                ant.append(j)
        isd = collections.Counter(ant)[1]
        return isd
        
    
    def cal_col(self,grid):
        res1 = []
        for i in zip(*grid):
            i = list(i)
            res1.append(i)
        return self.cal_len(res1)
        
    def islandPerimeter(self,grid):
        res = 0
        res = 4*(self.pre(grid))- 2*(self.cal_col(grid)) - 2*(self.cal_len(grid))
        return res







#Solution 2
def islandPerimeter(grid):
    if not grid:
        return 0
    width = len(grid[0])
    height = len(grid)
    cnt = 0
    dec = 0
    for i in xrange(0, height):
        for j in xrange(0, width):
            if grid[i][j] == 1:
                cnt += 1
                if j != width - 1 and grid[i][j+1] == 1:
                    print grid[i][j+1]
                    dec += 1    #continuous 1 in x axis
                if i != height -1 and grid[i+1][j] == 1:
                    dec += 1    #continuous 1 in y axis
    return 4*cnt - 2*dec
    
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
islandPerimeter(grid)
        
        
