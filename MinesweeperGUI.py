import sys
import tkinter as tk
from tkinter import ttk, messagebox
from Board import Board
from Player import Player

class MinesweeperGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper - Start Game")
        self.BuildStartScreen()

    def BuildStartScreen(self):
        ttk.Label(self.root, text="Enter Board Size (5-20):").pack(pady=10)
        self.sizeEntry = ttk.Entry(self.root)
        self.sizeEntry.pack(pady=5)
        self.sizeEntry.insert(0, "8")

        ttk.Label(self.root, text="Enter Difficulty (.1 to .9):").pack(pady=10)
        self.difficultyEntry = ttk.Entry(self.root)
        self.difficultyEntry.pack(pady=5)
        self.difficultyEntry.insert(0, "0.2")

        ttk.Button(self.root, text="Start Game", command=self.OnStartClick).pack(pady=20)
        ttk.Button(self.root, text="Quit", command=sys.exit).pack(pady=5)

        self.root.mainloop()

    def OnStartClick(self):
        try:
            size = int(self.sizeEntry.get())
            difficulty = float(self.difficultyEntry.get())
            if size < 5 or size > 20:
                messagebox.showerror("Invalid size", "Please enter a size between 5 and 20.")
                return
            if not (.1 <= difficulty <= .9):
                messagebox.showerror("Invalid difficulty", "Please enter a difficulty between .1 and .9.")
                return
            self.root.quit()
            self.root.destroy()
            self.StartGame(size, difficulty)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for size and difficulty.")

    def StartGame(self, size, difficulty, seed=0):
        self.gameRoot = tk.Tk()
        self.gameRoot.title("Minesweeper")
        self.player = Player(size,difficulty,seed)
        self.size = size
        self.buttons = [[None for _ in range(size)] for _ in range(size)]

        self.InitStyle()
        self.InitButtons()
        self.Refresh()

        self.gameRoot.mainloop()

    def InitStyle(self):
        style = ttk.Style()
        style.configure('TButton',
                        font=('Arial', 12, 'bold'),
                        padding=5,
                        width=4,
                        relief="flat",
                        background="#F0F0F0",
                        foreground="black")
        style.map('TButton', background=[('active', '#4CAF50'), ('pressed', '#45a049')])
        self.gameRoot.configure(bg='#D9E2F3')

    def InitButtons(self):
        for i in range(self.size):
            for j in range(self.size):
                btn = tk.Button(self.gameRoot, width=3, height=1, font=('Arial', 12, 'bold'))
                btn.grid(row=i, column=j)
                btn.bind('<Button-1>', lambda _, x=i, y=j: self.OnLeftClick(x, y))
                btn.bind('<Button-3>', lambda _, x=i, y=j: self.OnRightClick(x, y))
                self.buttons[i][j] = btn

    def OnLeftClick(self, x, y):
        result = self.player.board.LClick(x, y)
        self.Refresh()

        if not result:
            self.RevealAll()
            messagebox.showinfo("Game Over", "You clicked a mine!")
            self.gameRoot.destroy()
            MinesweeperGUI()
            return

        if self.player.CheckWin():
            self.RevealAll()
            messagebox.showinfo("You Win!", "Congratulations! You cleared the board.")
            self.gameRoot.destroy()
            MinesweeperGUI()

    def OnRightClick(self, x, y):
        self.player.board.RClick(x, y)
        self.Refresh()

        if self.player.CheckWin():
            self.RevealAll()
            messagebox.showinfo("You Win!", "Congratulations! You cleared the board.")
            self.gameRoot.destroy()
            MinesweeperGUI()

    def Refresh(self):
        for i in range(self.size):
            for j in range(self.size):
                tile = self.player.board.board[i][j]
                btn = self.buttons[i][j]
                if tile.isRevealed and tile.mineCount > 0:
                    btn.config(text=tile.mineCount, state="disabled", relief="sunken", bg="lightgrey")
                elif tile.isRevealed:
                    btn.config(text=" ", state="disabled", relief="sunken", bg="lightgrey")
                elif tile.isFlagCovered:
                    btn.config(text="F", fg="red", bg="#D9E2F3")
                else:
                    btn.config(text="", fg="black", bg="#E1EFFF")

    def RevealAll(self):
        for i in range(self.size):
            for j in range(self.size):
                tile = self.player.board.board[i][j]
                btn = self.buttons[i][j]
                if tile.isMine:
                    btn.config(text="*", fg="white", bg="red")
                elif tile.isFlagCovered:
                    btn.config(text="F", fg="red")
                elif tile.isRevealed and tile.mineCount > 0:
                    btn.config(text=tile.mineCount, state="disabled", relief="sunken", bg="lightgrey")
                elif tile.isRevealed:
                    btn.config(text=" ", state="disabled", relief="sunken", bg="lightgrey")

