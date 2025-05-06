from Tile import Tile
import random

class Board:
    def __init__(self,size):
        self.size = size
        self.board = self.MakeBoard(size)
        self.minesLeft = 0

    def CheckMines(self):
        self.minesLeft=0
        for row in self.board:
            for cell in row:
                if cell.isMine and not cell.isFlagCovered:
                    self.minesLeft= self.minesLeft+1 
                elif cell.isFlagCovered and not cell.isMine:
                    self.minesLeft= self.minesLeft+1 
        # print(self.__str__())
        # print(self.minesLeft)
        return self.minesLeft

    def MakeBoard(self,size):
        tmpBoard =  [[Tile() for _ in range(size)] for _ in range(size)]
        for i in range(len(tmpBoard)):
            for j in range(len(tmpBoard[0])):
                tmpBoard[i][j].location=[i,j]
        return tmpBoard

    def AddMines(self,difficulty = .2,seed = 0):
        if(seed!=0):
            random.seed(seed)
        if(difficulty>.9):
            difficulty=.9
        total = int(difficulty*self.size*self.size)
        if(total==0):
            total=1

        while(total>0):
            row = random.choice(self.board)
            cell = random.choice(row)
            if(cell.isMine):
                continue
            cell.isMine=True
            total-=1

    def LClick(self,x,y):
        return self.board[x][y].LClick(self)
        
    def RClick(self,x,y):
        return self.board[x][y].RClick()

    def __str__(self):
        result = ""
        result+="_"*(4+self.board.__len__())+"\n"
        for row in self.board:
            result+="| "
            for cell in row:
                result+=str(cell)
            result+=" |\n"
        result+="-"*(4+self.board.__len__())+"\n"
        return result
    
    def PlayerStr(self):
        result = ""
        for row in self.board:
            for cell in row:
                result+=cell.PlayerStr()
            result+="\n"
        return result