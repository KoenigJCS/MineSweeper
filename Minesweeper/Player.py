from Board import Board

class Player:
    def __init__(self,board):
        self.totalWins = 0
        self.board : Board = board
        self.difficulty = .3
        self.boardSize = 10

    def CheckWin(self):
        if(self.board.checkMines()==0):
            self.totalWins+=1
            return True
        return False
    
    def Reset(self,seed = -1):
        board = Board(self.boardSize)
        board.AddMines(self.difficulty,seed)

    def ProcessMove(self,x,y,isLClick):
        safe = True
        if(x<0 or y<0 or x>=self.boardSize or y>=self.boardSize):
            return ValueError("Invalid Input")
        elif(isLClick):
            safe = self.board.LClick(x,y)
        else:
            safe = self.board.RClick(x,y)
        
        return safe
