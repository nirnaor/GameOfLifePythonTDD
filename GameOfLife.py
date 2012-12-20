import pdb
import os
import time

"""
Represents a cell on the board of game of life. It's only uses 
are to determine the if and why a cell should live or die 
"""
class Cell:


    def __init__(self, value, neighbours_count):
        self.neighbours_count = neighbours_count
        self.value = value

    @property
    def is_alive_and_should_die_from_under_population(self):
        return self.value == 1 and self.neighbours_count < 2
    
    @property
    def is_alive_and_should_die_by_over_crowding(self):
        return self.value == 1 and self.neighbours_count > 3

    @property
    def is_alive_and_should_stay_alive(self):
        return self.value == 1 and ( self.neighbours_count == 2 or
                                     self.neighbours_count == 3)

    @property
    def is_dead_and_shoule_be_revived_by_reproduction(self):
        return self.value == 0 and self.neighbours_count == 3


"""
Holds the entire logic of Game of life. 
Has functionallity for adding new cells, and evolving due to the rules
of the game
"""
class GameOfLife:


    def __init__(self, size):
        if isinstance(size, int) == False:
            raise TypeError("size of board should be an integer")
        elif size < 1:
            raise ValueError("board size should be at least 1")
        self.size = size
        self._build_matrix()

    def _build_matrix(self):
        # Cell that is dead is assigned to value of 0
        self.board = []
        for i in range(self.size):
            self.board.append([0] * self.size)

        

    def add_living_cell(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        self.board[x][y] = 1 # Cell that is alive is assigned to value of 1
        return True

    def is_alive(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        return self.board[x][y] == 1

    def evolve(self):
        cells_to_revive = []
        cells_to_kill = []

        for x_axis in range(self.size):
            for y_axis in range(self.size):
                cell = self._get_cell(x_axis, y_axis)

                if cell.is_alive_and_should_die_from_under_population:
                        cells_to_kill.append([x_axis, y_axis])
                elif cell.is_alive_and_should_die_by_over_crowding:
                        cells_to_kill.append([x_axis, y_axis])
                elif cell.is_dead_and_shoule_be_revived_by_reproduction:
                        cells_to_revive.append([x_axis, y_axis])

        self._set_these_cells_to(1, cells_to_revive)
        self._set_these_cells_to(0, cells_to_kill)

    def _get_cell(self, x_axis, y_axis):
        return Cell(self.board[x_axis][y_axis],
                    self.neighbours_count(x_axis, y_axis))

    def _set_these_cells_to(self, value_to_set, cells_to_change):
        for each_cell in cells_to_change:
            x = each_cell[0]
            y = each_cell[1] 
            self.board[x][y] = value_to_set

    def _validate_that_coordinate_is_in_range(self, coordinate):
        if (coordinate < 0 or coordinate > self.size - 1):
            raise ValueError("board size is " + str(self.size)  + 
                    " and given coordinate is " + str(coordinate))

    def neighbours_count(self, x, y):
        neighbours_count = 0

        # one row above
        neighbours_count += self._get_value_safely(x - 1, y- 1)
        neighbours_count += self._get_value_safely(x, y- 1)
        neighbours_count += self._get_value_safely(x + 1, y- 1)

        # same row
        neighbours_count += self._get_value_safely(x - 1, y)
        neighbours_count += self._get_value_safely(x + 1, y)

        # one row below
        neighbours_count += self._get_value_safely(x - 1, y + 1)
        neighbours_count += self._get_value_safely(x, y + 1)
        neighbours_count += self._get_value_safely(x + 1, y + 1)

        return neighbours_count

    def _get_value_safely(self, x, y):
        try:
            return self.board[x][y]
        except IndexError as err:
            return 0

    def _draw_matrix(self):
        for x_axis in range(self.size):
            s = ""
            for y_axis in range(self.size):
                s += str(self.board[x_axis][y_axis])
            print(s)

    def draw_matrix_forever(self):
        while True:
            os.system('clear')
            self._draw_matrix()
            self.evolve()
            time.sleep(1)

