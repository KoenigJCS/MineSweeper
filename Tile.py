class Tile:
    def __init__(self):
        self.isMine = False
        self.location = [0,0]
        self.isFlagCovered = False
        self.isRevealed = False
        self.mineCount = 0

    def MakeMine(self):
        self.isMine= True

    def UnMakeMine(self):
        self.isMine= False

    def LClick(self,board):
        if(self.isFlagCovered):
            return True
        elif(self.isMine):
            return False
        else:
            self.isRevealed = True
            self.reveal_neighbors(board)
            return True
        
    def reveal_neighbors(self, board):
        rows = len(board.board)
        cols = len(board.board[0])
        x, y = self.location
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        self.mineCount = 0
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbor = board.board[nx][ny]
                neighbors.append(neighbor)
                if neighbor.isMine:
                    self.mineCount += 1

        if self.mineCount == 0:
            for neighbor in neighbors:
                if not neighbor.isRevealed and not neighbor.isMine and not neighbor.isFlagCovered:
                    neighbor.isRevealed = True
                    neighbor.reveal_neighbors(board)
        
    def RClick(self):
        if not self.isRevealed:
            self.isFlagCovered = not self.isFlagCovered
        
    def __str__(self):
        return "F" if self.isFlagCovered else ("X" if self.isMine else (str(self.mineCount) if self.mineCount>0 else " "))
    
    def PlayerStr(self):
        return "F" if self.isFlagCovered else self.mineCount if self.mineCount>0 else " "