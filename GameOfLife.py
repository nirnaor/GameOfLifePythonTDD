import pdb
class GameOfLife:

    def __init__(self, size):
        if isinstance(size, int) == False:
            raise TypeError("size of board should be an integer")
        elif size < 1:
            raise ValueError("board size should be at least 1")
        else:
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
        for x_axis in range(self.size):
            for y_axis in range(self.size):
                if self.board[x_axis][y_axis] == 1:
                    if self.neighbours_count(x_axis, y_axis) < 2:
                        self.board[x_axis][y_axis] = 0


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
            



