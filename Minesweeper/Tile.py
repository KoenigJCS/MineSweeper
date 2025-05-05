class Tile:
    def __init__(self):
        self.isMine = False
        self.location = [0,0]
        self.isFlagCovered = False
        self.isRevealed = False

    def MakeMine(self):
        self.isMine= True

    def UnMakeMine(self):
        self.isMine=0

    def LClick(self):
        if(self.isFlagCovered):
            return True
        elif(self.isMine):
            return False
        else:
            self.isRevealed=True
            return True
        
    def RClick(self):
        if not self.isRevealed:
            self.isFlagCovered = not self.isFlagCovered
        
    def __str__(self):
        return "F" if self.isFlagCovered else "X" if self.isMine else  "-" 
    
    def PlayerStr(self):
        return "F" if self.isFlagCovered else  "-" 