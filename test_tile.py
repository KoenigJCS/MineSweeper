import unittest
from Tile import Tile

class MockBoard:
    def __init__(self, rows, cols):
        self.board = [[Tile() for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.board[i][j].location = [i, j]

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile()
        self.board = MockBoard(3, 3)

    def test_make_and_unmake_mine(self):
        self.assertFalse(self.tile.isMine)
        self.tile.MakeMine()
        self.assertTrue(self.tile.isMine)
        self.tile.UnMakeMine()
        self.assertFalse(self.tile.isMine)

    def test_right_click_toggle_flag(self):
        self.tile.RClick()
        self.assertTrue(self.tile.isFlagCovered)
        self.tile.RClick()
        self.assertFalse(self.tile.isFlagCovered)

    def test_right_click_does_not_work_if_revealed(self):
        self.tile.isRevealed = True
        self.tile.RClick()
        self.assertFalse(self.tile.isFlagCovered)

    def test_lclick_on_flagged_tile(self):
        self.tile.isFlagCovered = True
        result = self.tile.LClick(self.board)
        self.assertTrue(result)

    def test_lclick_on_mine_tile(self):
        self.tile.isMine = True
        result = self.tile.LClick(self.board)
        self.assertFalse(result)

    def test_lclick_reveals_tile_and_neighbors(self):
        center = self.board.board[1][1]
        result = center.LClick(self.board)
        self.assertTrue(center.isRevealed)
        self.assertTrue(result)
        for row in self.board.board:
            for tile in row:
                self.assertTrue(tile.isRevealed)

    def test_lclick_with_adjacent_mine(self):
        self.board.board[0][0].MakeMine()
        tile = self.board.board[0][1]
        tile.LClick(self.board)
        self.assertEqual(tile.mineCount, 1)
        self.assertTrue(tile.isRevealed)

    def test_str_methods(self):
        tile = Tile()
        self.assertEqual(str(tile), " ")
        tile.mineCount = 2
        self.assertEqual(str(tile), "2")
        tile.MakeMine()
        self.assertEqual(str(tile), "X")
        tile.isMine = False
        tile.isFlagCovered = True
        self.assertEqual(str(tile), "F")

    def test_player_str(self):
        tile = Tile()
        tile.isFlagCovered = True
        self.assertEqual(tile.PlayerStr(), "F")
        tile.isFlagCovered = False
        tile.mineCount = 3
        self.assertEqual(tile.PlayerStr(), 3)
        tile.mineCount = 0
        self.assertEqual(tile.PlayerStr(), " ")

if __name__ == '__main__':
    unittest.main()
