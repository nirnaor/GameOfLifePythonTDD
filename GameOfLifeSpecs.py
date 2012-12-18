import unittest
from GameOfLife import GameOfLife


class TestInitMethod(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)

    def test_that__it_initializes_board_size(self):
        self.assertEqual(self.game.size, 5)

    def test_that_it_raises_type_error_when_size_is_not_a_number(self):
        with self.assertRaises(TypeError):
            game_without_size = GameOfLife('2')

    def test_that_it_raises_value_error_when_size_is_not_a_number(self):
        with self.assertRaises(ValueError):
            game_without_size = GameOfLife(0)


class TestAddLivingCellMethod(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)

    def test_that_it_raises_value_error_when_x_is_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(5,0)
    def test_that_it_raises_value_error_when_y_is_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(2,5)
    def test_that_it_raises_value_error_when_both_are_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(7,5)


if __name__ == '__main__':
    unittest.main()
