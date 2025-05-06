import unittest
from unittest.mock import patch, MagicMock
# import tkinter as tk
from MinesweeperGUI import MinesweeperGUI

class TestMinesweeperGUI(unittest.TestCase):
    def setUp(self):
        self.mock_tk = MagicMock()
        self.mock_tk.mainloop = MagicMock()
        self.mock_tk.title = MagicMock()
        self.mock_tk.quit = MagicMock()
        self.mock_tk.destroy = MagicMock()
        self.mock_tk.destroy = MagicMock()
        patcher = patch('tkinter.Tk', return_value=self.mock_tk)
        self.addCleanup(patcher.stop)
        patcher.start()
        self.gui = MinesweeperGUI()
        self.gui.sizeEntry = MagicMock()
        self.gui.difficultyEntry = MagicMock()

    def test_on_start_click_valid_input(self):
        self.gui.sizeEntry.get.return_value = '10'
        self.gui.difficultyEntry.get.return_value = '0.3'
        with patch.object(self.gui, 'StartGame') as mock_start:
            self.gui.OnStartClick()
            mock_start.assert_called_once_with(10, 0.3)

    def test_on_start_click_invalid_size(self):
        self.gui.sizeEntry.get.return_value = '3'
        self.gui.difficultyEntry.get.return_value = '0.3'
        with patch('tkinter.messagebox.showerror') as mock_err:
            self.gui.OnStartClick()
            mock_err.assert_called_once_with("Invalid size", "Please enter a size between 5 and 20.")
        self.gui.sizeEntry.get.return_value = '21'
        self.gui.difficultyEntry.get.return_value = '0.3'
        with patch('tkinter.messagebox.showerror') as mock_err:
            self.gui.OnStartClick()
            mock_err.assert_called_once_with("Invalid size", "Please enter a size between 5 and 20.")

    def test_on_start_click_invalid_difficulty(self):
        self.gui.sizeEntry.get.return_value = '10'
        self.gui.difficultyEntry.get.return_value = '0.05'
        with patch('tkinter.messagebox.showerror') as mock_err:
            self.gui.OnStartClick()
            mock_err.assert_called_once_with("Invalid difficulty", "Please enter a difficulty between .1 and .9.")
        self.gui.sizeEntry.get.return_value = '10'
        self.gui.difficultyEntry.get.return_value = '1.0'
        with patch('tkinter.messagebox.showerror') as mock_err:
            self.gui.OnStartClick()
            mock_err.assert_called_once_with("Invalid difficulty", "Please enter a difficulty between .1 and .9.")

    def test_on_start_click_non_numeric(self):
        self.gui.sizeEntry.get.return_value = 'a'
        self.gui.difficultyEntry.get.return_value = 'b'
        with patch('tkinter.messagebox.showerror') as mock_err:
            self.gui.OnStartClick()
            mock_err.assert_called_once_with("Invalid input", "Please enter valid numbers for size and difficulty.")

    @patch('MinesweeperGUI.MinesweeperGUI.InitStyle', MagicMock(return_value=None))
    def test_start_game_creates_buttons(self):
        self.gui.StartGame(4, 0.2, 42)
        self.assertEqual(len(self.gui.buttons), 4)
        self.assertEqual(len(self.gui.buttons[0]), 4)

    @patch('MinesweeperGUI.MinesweeperGUI.InitStyle', MagicMock(return_value=None))
    def test_refresh_and_reveal_all_integration(self):
        self.gui.StartGame(3, 0.1, 42)
        board = self.gui.player.board.board
        board[0][0].isRevealed = True
        board[0][0].mineCount = 1
        # call refresh
        try:
            self.gui.Refresh()
            self.gui.RevealAll()
        except Exception as e:
            self.fail(f"Refresh or RevealAll raised {e}")

    @patch('MinesweeperGUI.MinesweeperGUI.InitStyle', MagicMock(return_value=None))
    def test_on_left_click_loss_and_restart(self):
        self.gui.StartGame(3, .9, 42)
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.gui.OnLeftClick(0, 0)
            mock_info.assert_called_once_with("Game Over", "You clicked a mine!")

    @patch('MinesweeperGUI.MinesweeperGUI.InitStyle', MagicMock(return_value=None))
    def test_on_left_click_win_and_restart(self):
        self.gui.StartGame(2, 0.0)
        board = self.gui.player.board.board
        for row in board:
            for t in row:
                t.isMine = False
                t.isRevealed = False
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.gui.OnLeftClick(0, 0)
            mock_info.assert_called_once_with("You Win!", "Congratulations! You cleared the board.")

    @patch('MinesweeperGUI.MinesweeperGUI.InitStyle', MagicMock(return_value=None))
    def test_on_right_click_flag_and_win(self):
        self.gui.StartGame(2, 0.1,42)
        board = self.gui.player.board.board
        for row in board:
            for t in row:
                if(t.isMine):
                    t.isFlagCovered = True
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.gui.OnRightClick(1, 1) # bad as it coveres un-mine tile on this seed
            self.gui.OnRightClick(1, 1)
            mock_info.assert_called_once_with("You Win!", "Congratulations! You cleared the board.")

if __name__ == '__main__':
    unittest.main()
