# TODO: configure number of bombs per difficulty, and add as member function called get_bomb_count
# TODO: disperse correct number of bombs within gameboard
# TODO: update non bomb board squares with correct values (bombs = 9, empty = 0)
# TODO: create board overlay that user interacts with
# TODO: implement functions for actions: guess empty box, guess numbered box, guess mine box, flag box 
# TODO: mine counter, restart functionlity, timer

class Difficulty:
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"

class GameBoard:
    def get_dimensions(self):
        match self.difficulty:
            case Difficulty.EXPERT:
                return [16, 30]
            case Difficulty.INTERMEDIATE:
                return [16, 16]
            case Difficulty.BEGINNER:
                return [9, 9]
            case _:
                return [9, 9]
    
    def update_difficulty(self, difficulty):
        self.difficulty = difficulty

    def create_board(self):
        board = []
        rows, cols = self.get_dimensions()     
        for row in range(rows):
            line = [0] * cols
            board.append(line)
        self.board = board
    
    def x(self):
        rows = self.board
        for row in self.board:
            for col in row:

    
    def display_board(self):
        for row in self.board:
            print(row)

    def __init__(self, difficulty=Difficulty.BEGINNER):
        self.update_difficulty(difficulty)
        self.create_board()
    
    
if __name__ == "__main__":
    board1 = GameBoard(Difficulty.BEGINNER)
    board1.display_board()