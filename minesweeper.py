import random

# TODO: timer - pygame
# TODO: restart functionality
# TODO: Mine counter, make mine counter a class member variable
# TODO: research pygame

class Difficulty:
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"

class GameBoard:
    class ActionTypes:
        GUESS = "guess"
        FLAG = "flag"

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
        board_list = []
        num_mine = self.get_mine_count()
        board_list.extend([self.MINE_INDICATOR] * num_mine)
        board_list.extend([self.DEFAULT_INDICATOR] * (total_cells - num_mine))
        '''for row in range(rows):
            line = [0] * cols
            board.append(line)'''
        random.shuffle(board_list)
        board = []
        canvas = []
        for row in range(rows):
            line = board_list[row * cols:(row * cols) + cols]
            board.append(line)
            canvas.append([-1] * cols)
        self.board = board
        self.canvas = canvas
    
    # TODO: abstract checking rows into a function, should be able to call function 3 times in update_tile_values

    def __update_tile_values(self):
        current_board = self.board
        number_of_rows = len(current_board)
        number_of_cols = len(current_board[0])
        for row in range(number_of_rows):   
            for col in range(number_of_cols):
                neighbors =  []
                if current_board[row][col] == self.MINE_INDICATOR:
                    continue
                previous_row = row - 1
                next_row = row + 1
                previous_col = col - 1
                next_col = col + 1
                # checking previous row
                if previous_row >= 0:
                    if previous_col >= 0:
                        neighbors.append(current_board[previous_row][previous_col])
                    neighbors.append(current_board[previous_row][col])
                    if next_col < number_of_cols:  
                        neighbors.append(current_board[previous_row][next_col])
                # checking current row
                if previous_col >= 0:
                    neighbors.append(current_board[row][previous_col])
                if next_col < number_of_cols:
                    neighbors.append(current_board[row][next_col])
                # checking next row
                if next_row < number_of_rows:
                    if previous_col >= 0:
                        neighbors.append(current_board[next_row][previous_col])
                    neighbors.append(current_board[next_row][col])
                    if next_col < number_of_cols:  
                        neighbors.append(current_board[next_row][next_col])
                # update current_board value
                nieghbor_mine_count = neighbors.count(self.MINE_INDICATOR)
                current_board[row][col] = nieghbor_mine_count

    def handle_action(self, row, col, action_type):
        match action_type:
            case self.ActionTypes.GUESS:
                self.handle_guess(row, col,)
            case self.ActionTypes.FLAG:
                self.handle_flag(row, col)
            case _:
                print("error: invalid action")

    # TODO: implement functions for actions: guess empty box - introduce recursion for handling empty guesses   
    def handle_guess(self, row, col):
        tile_value = self.board[row][col]
        if tile_value == self.DEFAULT_INDICATOR:
            # expose box as well as any adjacent or diagonal empty spots

            print("empty tile selected")
        elif tile_value == self.MINE_INDICATOR:
            # end game and update canvas with all mines
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == self.MINE_INDICATOR:
                        self.canvas[row][col] = self.MINE_INDICATOR
            print("GAME OVER")
        else:
            self.canvas[row][col] = tile_value

    def handle_flag(self, row, col):
        print("handling flag")


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

    def display_canvas(self):
        for row in self.canvas:
            print(row)

    def __init__(self, difficulty=Difficulty.BEGINNER):
        self.update_difficulty(difficulty)
        self.mine_count = self.get_mine_count()
        self.create_board()
        self.__update_tile_values()

        
if __name__ == "__main__":
    board1 = GameBoard(Difficulty.BEGINNER)
    board1.display_board()
    print("-----")
    board1.handle_guess(1, 1)
    board1.display_canvas()
