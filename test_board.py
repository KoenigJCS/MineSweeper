import unittest
from Board import Board

class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = Board(5)
        self.assertEqual(board.size, 5)
        self.assertEqual(len(board.board), 5)
        self.assertEqual(len(board.board[0]), 5)
        for i in range(5):
            for j in range(5):
                self.assertEqual(board.board[i][j].location, [i, j])

    def test_add_mines(self):
        board = Board(5)
        board.AddMines(difficulty=0.2, seed=42)
        mine_count = sum(cell.isMine for row in board.board for cell in row)
        expected = int(0.2 * 25)
        self.assertEqual(mine_count, expected)

    def test_add_mines_with_seed(self):
        board1 = Board(5)
        board1.AddMines(difficulty=0.2, seed=42)
        mine_count1 = sum(cell.isMine for row in board1.board for cell in row)
        board2 = Board(5)
        board2.AddMines(difficulty=0.2, seed=42)
        mine_count2 = sum(cell.isMine for row in board2.board for cell in row)
        self.assertEqual(mine_count1,mine_count2)
        for i in range(5):
            for j in range(5):
                self.assertEqual(board1.board[i][j].isMine, board2.board[i][j].isMine)

    def test_add_mines_extreme_difficulty(self):
        board = Board(5)
        board.AddMines(difficulty=1.5)
        mine_count = sum(cell.isMine for row in board.board for cell in row)
        expected = int(0.9 * 25)
        self.assertEqual(mine_count, expected)

    def test_add_mines_minimum_one(self):
        board = Board(5)
        board.AddMines(difficulty=0.0)
        mine_count = sum(cell.isMine for row in board.board for cell in row)
        self.assertEqual(mine_count, 1)

    def test_check_mines_counts_remaining(self):
        board = Board(5)
        board.AddMines(difficulty=0.2, seed=123)
        mineCount = board.CheckMines()

        self.assertGreaterEqual(mineCount, 0)
        flaggedWrong = sum(cell.isFlagCovered and not cell.isMine for row in board.board for cell in row)
        unflaggedMines = sum(cell.isMine and not cell.isFlagCovered for row in board.board for cell in row)
        self.assertEqual(mineCount, flaggedWrong + unflaggedMines)

    def test_left_click_safe(self):
        board = Board(5)
        board.AddMines(difficulty=0.1, seed=1)
        
        for i in range(5):
            for j in range(5):
                if not board.board[i][j].isMine:
                    result = board.LClick(i, j)
                    self.assertTrue(result)
                    self.assertTrue(board.board[i][j].isRevealed)
                    return

    def test_left_click_mine(self):
        board = Board(5)
        board.AddMines(difficulty=.9, seed=99)
        # on this seed 0,0 is mine
        result = board.LClick(0, 0)
        self.assertFalse(result)

    def test_right_click_toggle(self):
        board = Board(5)
        cell = board.board[2][2]
        self.assertFalse(cell.isFlagCovered)
        board.RClick(2, 2)
        self.assertTrue(cell.isFlagCovered)
        board.RClick(2, 2)
        self.assertFalse(cell.isFlagCovered)

    def test_str_representation(self):
        board = Board(3)
        output = str(board)
        self.assertIn("|", output)
        self.assertIn("_", output)
        self.assertIn("-", output)
        self.assertEqual(output.count("\n"), 5)

    def test_player_str_representation(self):
        board = Board(3)
        output = board.PlayerStr()
        self.assertEqual(len(output.splitlines()), 3)

if __name__ == "__main__":
    unittest.main()
