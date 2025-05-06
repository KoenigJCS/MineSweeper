import unittest
from Player import Player

class TestPlayer(unittest.TestCase):

    def test_initialization_defaults(self):
        player = Player()
        self.assertEqual(player.totalWins, 0)
        self.assertEqual(player.difficulty, 0.3)
        self.assertEqual(player.boardSize, 10)
        self.assertEqual(len(player.board.board), 10)
        self.assertTrue(any(cell.isMine for row in player.board.board for cell in row))

    def test_initialization_custom(self):
        player = Player(boardSize=5, difficulty=0.5, seed=42)
        self.assertEqual(player.boardSize, 5)
        self.assertEqual(player.difficulty, 0.5)
        self.assertEqual(len(player.board.board), 5)

    def test_check_win_true(self):
        player = Player(boardSize=3, difficulty=0.0)
        for row in player.board.board:
            for cell in row:
                if cell.isMine:
                    cell.isFlagCovered = True
        result = player.CheckWin()
        self.assertTrue(result)
        self.assertEqual(player.totalWins, 1)

    def test_check_win_false(self):
        player = Player(boardSize=3, difficulty=0.2, seed=1)
        result = player.CheckWin()
        self.assertFalse(result)
        self.assertEqual(player.totalWins, 0)

    def test_reset_changes_board(self):
        player = Player(boardSize=4, difficulty=0.3, seed=1)
        original_board_str = str(player.board)
        player.Reset(seed=2)
        new_board_str = str(player.board)
        self.assertNotEqual(original_board_str, new_board_str)

    def test_process_move_left_click_safe(self):
        player = Player(boardSize=5, difficulty=0.1, seed=3)
        for i in range(5):
            for j in range(5):
                if not player.board.board[i][j].isMine:
                    result = player.ProcessMove(i, j, isLeftClick=True)
                    self.assertTrue(result)
                    self.assertTrue(player.board.board[i][j].isRevealed)
                    return

    def test_process_move_left_click_mine(self):
        player = Player(boardSize=5, difficulty=1.0, seed=1)
        # on this seed 0,0 is mine
        result = player.ProcessMove(0, 0, isLeftClick=True)
        self.assertFalse(result)

    def test_process_move_right_click(self):
        player = Player(boardSize=4, difficulty=0.0)
        player.ProcessMove(1, 1, isLeftClick=False)
        self.assertTrue(player.board.board[1][1].isFlagCovered)

    def test_process_move_invalid_coordinates(self):
        player = Player()
        with self.assertRaises(ValueError):
            player.ProcessMove(-1, 0, True)
        with self.assertRaises(ValueError):
            player.ProcessMove(0, -1, True)
        with self.assertRaises(ValueError):
            player.ProcessMove(player.boardSize, 0, True)
        with self.assertRaises(ValueError):
            player.ProcessMove(0, player.boardSize, True)

if __name__ == "__main__":
    unittest.main()
