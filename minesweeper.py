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
    FLAG_INDICATATOR = -2
    UNGUESSED_INDICATOR = -1
    visited = []

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
            canvas.append([self.UNGUESSED_INDICATOR] * cols)
        self.board = board
        self.canvas = canvas

    def __check_neighbor_values(self, row, col, number_of_cols, current_board, ignore_current_col=False):
        neighbors = []
        # previous col
        if col - 1 >= 0:
            neighbors.append(current_board[row][col - 1])
        # current col - need to handle when function is used on current col
        if not ignore_current_col:
            neighbors.append(current_board[row][col])
        # next col
        if col + 1 < number_of_cols:
            neighbors.append(current_board[row][col + 1])
        return neighbors

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
                # checking previous row
                if previous_row >= 0:
                    neighbors.extend(self.__check_neighbor_values(previous_row, col, number_of_cols, current_board))
                # checking current row
                neighbors.extend(self.__check_neighbor_values(row, col, number_of_cols, current_board, True))
                # checking next row
                if next_row < number_of_rows:
                    neighbors.extend(self.__check_neighbor_values(next_row, col, number_of_cols, current_board))
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

    def __get_row_neighbors(self, row_index, col_index, number_of_cols, current_board, ignore_current_col=False):
        indices_values = []
        previous_col = col_index - 1
        next_col = col_index + 1
        # previous col
        if previous_col >= 0:
            indices_values.append(([row_index, previous_col], current_board[row_index][previous_col]))
        # current col
        if not ignore_current_col:
            indices_values.append(([row_index, col_index], current_board[row_index][col_index]))
        # next col
        if next_col < number_of_cols:
            indices_values.append(([row_index, next_col], current_board[row_index][next_col]))
        return indices_values

    def __get_neighbors(self, row_index, col_index):
        # find the index and value of all the neighbors, add the index to the return list
        current_board = self.board
        neighbors = []
        previous_row = row_index - 1
        next_row = row_index + 1
        number_of_cols = len(current_board[0])
        number_of_rows = len(current_board)
        # checking previous row
        if previous_row >= 0:
            neighbors.extend(self.__get_row_neighbors(previous_row, col_index, number_of_cols, current_board))
        # checking current row
        neighbors.extend(self.__get_row_neighbors(row_index, col_index, number_of_cols, current_board, True))
        # checking next row
        if next_row < number_of_rows:
            neighbors.extend(self.__get_row_neighbors(next_row, col_index, number_of_cols, current_board))
        return neighbors
    
    def find_indices_to_expose(self, current_coords):
        if current_coords in self.visited:
            return
        self.visited.append(current_coords)
        indices = []
        neighbors = self.__get_neighbors(current_coords[0], current_coords[1])
        for neighbor in neighbors:
            coords = neighbor[0] 
            value = neighbor[1]
            indices.append(coords)
            if value != 0 or coords in self.visited:
                continue
            else:
                indices.extend(self.find_indices_to_expose(coords))
        return indices

    def handle_empty_square_guess(self, row_index, col_index):
        indices = self.find_indices_to_expose([row_index, col_index])
        for coords in indices:
            self.canvas[coords[0]][coords[1]] = self.board[coords[0]][coords[1]]
 
    def handle_guess(self, row, col):
        tile_value = self.board[row][col]
        if tile_value == self.DEFAULT_INDICATOR:
            self.handle_empty_square_guess(row, col)
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

    def restart_game(self):
        # function to restart the game when the restart button is clicked
        # likely need to put all the game functions within a loop to restart, a restart function may not work
        self.visited = []
        print("restart")
    
    def mine_counter(self, mine_count):
        # function to display remaining mines/flags and update when user lays down flag
        print("mine counter")

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
