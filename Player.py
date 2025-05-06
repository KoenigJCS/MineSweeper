from Board import Board

class Player:
    def __init__(self, boardSize=10, difficulty=0.3,seed = 0):
        self.totalWins = 0
        self.difficulty = difficulty
        self.boardSize = boardSize
        self.board = Board(boardSize)
        self.board.AddMines(difficulty,seed)

    def CheckWin(self):
        if self.board.CheckMines() == 0:
            self.totalWins += 1
            return True
        return False

    def Reset(self, seed=0):
        self.board = Board(self.boardSize)
        self.board.AddMines(self.difficulty, seed)

    def ProcessMove(self, x, y, isLeftClick):
        if x < 0 or y < 0 or x >= self.boardSize or y >= self.boardSize:
            raise ValueError("Invalid Input")
        if isLeftClick:
            return self.board.LClick(x, y)
        else:
            return self.board.RClick(x, y)