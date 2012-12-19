from GameOfLife import GameOfLife
class Patterns:
    @staticmethod
    def blinker():
        game = GameOfLife(6)
        game.add_living_cell(3, 2)
        game.add_living_cell(3, 3)
        game.add_living_cell(3, 4)
        return game

    @staticmethod
    def toad():
        game = GameOfLife(6)

        game.add_living_cell(2, 2)
        game.add_living_cell(3, 2)
        game.add_living_cell(4, 2)
        
        game.add_living_cell(1, 3)
        game.add_living_cell(2, 3)
        game.add_living_cell(3, 3)
        return game

    @staticmethod
    def beacon():
        game = GameOfLife(6)

        game.add_living_cell(1, 1)
        game.add_living_cell(2, 1)
        game.add_living_cell(1, 2)
        
        game.add_living_cell(4, 3)
        game.add_living_cell(3, 4)
        game.add_living_cell(4, 4)
        return game
