# import sys
# from Board import Board
# import tkinter as tk
# from tkinter import ttk, messagebox
from MinesweeperGUI import MinesweeperGUI

def main():
    MinesweeperGUI()
    # show_start_screen()

# def StartGame(size,difficulty,seed = -1):
#     root = tk.Tk()
#     root.title("Minesweeper")
#     board = Board(size)
#     board.AddMines(difficulty, seed)
#     buttons = [[None for _ in range(size)] for _ in range(size)]
#     gameOver=False

#     style = ttk.Style()
#     style.configure('TButton',
#                     font=('Arial', 12, 'bold'),
#                     padding=5,
#                     width=4,
#                     relief="flat",
#                     background="#F0F0F0",
#                     foreground="black")
#     style.map('TButton', background=[('active', '#4CAF50'), ('pressed', '#45a049')])
#     root.configure(bg='#D9E2F3')

#     def refresh():
#         for i in range(size):
#             for j in range(size):
#                 tile = board.board[i][j]
#                 btn = buttons[i][j]
#                 if tile.isRevealed and tile.mineCount > 0:
#                     btn.config(text=tile.mineCount, state="disabled", relief="sunken", bg="lightgrey")
#                 elif tile.isRevealed:
#                     btn.config(text=" ", state="disabled", relief="sunken", bg="lightgrey")
#                 elif tile.isFlagCovered:
#                     btn.config(text="F", fg="red", bg="#D9E2F3")
#                 else:
#                     btn.config(text="", fg="black", bg="#E1EFFF")

#     def reveal_all():
#         for i in range(size):
#             for j in range(size):
#                 tile = board.board[i][j]
#                 btn = buttons[i][j]
#                 if tile.isMine:
#                     btn.config(text="*", fg="white", bg="red")
#                 elif tile.isFlagCovered:
#                     btn.config(text="F", fg="red")
#                 elif tile.isRevealed and tile.mineCount > 0:
#                     btn.config(text=tile.mineCount, state="disabled", relief="sunken", bg="lightgrey")
#                 elif tile.isRevealed:
#                     btn.config(text=" ", state="disabled", relief="sunken", bg="lightgrey")

#     def on_left_click(x, y):
#         result = board.LClick(x, y)
#         refresh()
#         if not result:
#             reveal_all()
#             messagebox.showinfo("Game Over", "You clicked a mine!")
#             root.destroy()  # Close game window
#             show_start_screen()  # Start over

#     def on_right_click(x, y):
#         board.RClick(x, y)
#         refresh()

#     for i in range(size):
#         for j in range(size):
#             btn = tk.Button(root, width=3, height=1, font=('Arial', 12, 'bold'))
#             btn.grid(row=i, column=j)
#             btn.bind('<Button-1>', lambda _, x=i, y=j: on_left_click(x, y))
#             btn.bind('<Button-3>', lambda _, x=i, y=j: on_right_click(x, y))
#             buttons[i][j] = btn

#     refresh()
#     root.mainloop()

# def show_start_screen():
#     start_window = tk.Tk()
#     start_window.title("Minesweeper - Start Game")

#     def on_start_button_click():
#         try:
#             size = int(size_entry.get())
#             difficulty = float(difficulty_entry.get())
#             if size < 5 or size > 20:
#                 messagebox.showerror("Invalid size", "Please enter a size between 5 and 20.")
#                 return
#             if not (0 < difficulty <= 1):
#                 messagebox.showerror("Invalid difficulty", "Please enter a difficulty between 0 and 1.")
#                 return
#             start_window.quit()
#             start_window.destroy()
#             StartGame(size, difficulty)
#         except ValueError:
#             messagebox.showerror("Invalid input", "Please enter valid numbers for size and difficulty.")

#     def quit():
#         sys.exit()

#     ttk.Label(start_window, text="Enter Board Size (5-20):").pack(pady=10)
#     size_entry = ttk.Entry(start_window)
#     size_entry.pack(pady=5)
#     size_entry.insert(0, "8")  # default size 8

#     ttk.Label(start_window, text="Enter Difficulty (0 to 1):").pack(pady=10)
#     difficulty_entry = ttk.Entry(start_window)
#     difficulty_entry.pack(pady=5)
#     difficulty_entry.insert(0, "0.2")  # default difficulty 0.2

#     start_button = ttk.Button(start_window, text="Start Game", command=on_start_button_click)
#     start_button.pack(pady=20)

#     start_button = ttk.Button(start_window, text="Quit", command=quit)
#     start_button.pack(pady=5)

#     start_window.mainloop()

if __name__ == "__main__":
    main()