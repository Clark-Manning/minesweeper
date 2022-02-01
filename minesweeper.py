import random

# TODO: configure number of bombs per difficulty, and add as member function called get_bomb_count
# TODO: disperse correct number of bombs within gameboard
# TODO: update non bomb board squares with correct values (bombs = 9, empty = 0)
# TODO: create board overlay that user interacts with
# TODO: implement functions for actions: guess empty box, guess numbered box, guess mine box, flag box 
# TODO: mine counter, restart functionality, timer

class Difficulty:
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"

class GameBoard:
    MINE_INDICATOR = 9
    DEFAULT_INDICATOR = 0

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
        rows, cols = self.get_dimensions() 
        total_cells = rows * cols
        board = []
        num_mine = self.get_mine_count()
        board.extend([self.MINE_INDICATOR] * num_mine)
        board.extend([DEFAULT_INDICATOR] * (total_cells - num_mine))
        '''for row in range(rows):
            line = [0] * cols
            board.append(line)'''
        random.shuffle(board)
        two_d_board = []
        for row in range(rows):
            line = board[row * cols:(row * cols) + cols]
            two_d_board.append(line)
        print(board)
        self.board = two_d_board
    
    def update_tile_values(self):
        current_board = self.board
        number_of_rows = len(current_board)
        number_of cols = len(row)
        for row in range(number_of_rows):
            for col in range(len(row)):
                neighbors =  []
                if current_board[row][col] == MINE_INDICATOR:
                    return
                previous_row = row - 1
                next_row = row + 1
                previous_col = col - 1
                next_col = col + 1
                if previous_row >= 0:
                    if previous_col >= 0:
                        neigbors.append(current_board[previous_row][previous_col])
                    neigbors.append(current_board[previous_row][col])
                    if next_col > number:
                        return
                    neigbors.append(current_board[previous_row][next_col])


            line = board[row * cols:(row * cols) + cols]
            two_d_board.append(line)

        '''previous row of current column index -1 through +1
        current row of current column index -1 and +1
        next row of current column index -1 through +1
        if row of interest is < 0 or >=  num of rows: ignore
        if column of interest is < 0 or >= num of cols: ignore
        then add value to list of find_neighbors
        check list of neighbors for num of mines and store var
        above var is the tiles new value'''




    
    '''def x(self):
        rows = self.board
        for row in self.board:
            for col in row:'''
    
    def get_mine_count(self):
        match self.difficulty:
            case Difficulty.EXPERT:
                return 99
            case Difficulty.INTERMEDIATE:
                return 40
            case Difficulty.BEGINNER:
                return 10
            case _:
                return 10
    
    def display_board(self):
        for row in self.board:
            print(row)

    def __init__(self, difficulty=Difficulty.BEGINNER):
        self.update_difficulty(difficulty)
        self.mine_count = self.get_mine_count()
        self.create_board()

        
    
    
if __name__ == "__main__":
    board1 = GameBoard(Difficulty.BEGINNER)
    board1.display_board()