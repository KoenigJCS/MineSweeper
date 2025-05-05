from Tile import Tile
import random

class Board:
    def __init__(self,size):
        self.size = size
        self.board = self.MakeBoard(size)
        self.minesLeft = 0

    def checkMines(self):
        for row in self.board:
            for cell in row:
                self.minesLeft+=1 if cell.isMine and not cell.isFlagCovered else 0

        return self.minesLeft

    def MakeBoard(self,size):
        return [[Tile() for _ in range(size)] for _ in range(size)]

    def AddMines(self,difficulty = .3,seed = -1):
        if(seed!=0):
            random.seed(seed)
        total = int(difficulty*self.size*self.size)
        while(total>0):
            row = random.choice(self.board)
            cell = random.choice(row)
            if(cell.isMine):
                continue
            cell.isMine=True
            total-=1

    def LClick(self,x,y):
        return self.board[x][y].LClick()
        
    def RClick(self,x,y):
        return self.board[x][y].RClick()

    def __str__(self):
        result = ""
        for row in self.board:
            for cell in row:
                result+=str(cell)
            result+="\n"
        return result
    
    def PlayerStr(self):
        result = ""
        for row in self.board:
            for cell in row:
                result+=cell.PlayerStr()
            result+="\n"
        return result