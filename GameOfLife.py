class GameOfLife:

    def __init__(self, size):
        if isinstance(size, int) == False:
            raise TypeError("size of board should be an integer")
        elif size < 1:
            raise ValueError("board size should be at least 1")
        else:
            self.size = size

    def add_living_cell(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)


    def _validate_that_coordinate_is_in_range(self, coordinate):
        if (coordinate < 1 or coordinate > self.size - 1):
            raise ValueError("board size is " + str(self.size)  + 
                    " and given coordinate is " + str(coordinate))

            



