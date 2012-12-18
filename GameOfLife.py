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
        self.board =  [[0] * self.size]  * self.size 
        

    def add_living_cell(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        self.board[x][y] = 1 # Cell that is alive is assigned to value of 1
        return True


    def _validate_that_coordinate_is_in_range(self, coordinate):
        if (coordinate < 1 or coordinate > self.size - 1):
            raise ValueError("board size is " + str(self.size)  + 
                    " and given coordinate is " + str(coordinate))

    def is_alive(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        return self.board[x][y] == 1

            



