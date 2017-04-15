def is_unit(self,unit):
    unit = [i for i in unit if i != "."]
    return len(set(unit)) == len(unit)
    
def is_raw(self,board):
    for i in board:
        if not self.is_unit(i):
            return False
    return True

def is_col(self,board):
    for i in zip(*board):
        if not self.is_unit(i):
            return False
    return True
def is_square(self,board):
    for x in (0,3,6):
        for y in (0,3,6):
            square = [board[i][j] for i in range(x,x+3) for j in range(y,y+3)]
            if not self.is_unit(square):
                return False 
    return True

def isValidSudoku(self, board):
    return (self.is_raw(board) and self.is_col(board) and self.is_square(board))


    
    


board = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[2,2,2,4,5,6,7,8,9],[2,2,2,4,5,6,7,8,9],[2,2,2,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
#s = [1,3,3,'.','.','.',6,7,8,'.']
#is_unit_valid(s)
