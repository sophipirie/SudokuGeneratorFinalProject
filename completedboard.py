from blankboard import BlankBoard
import random
import numpy as np
from copy import deepcopy

class CompletedBoard(BlankBoard):
    def __init__(self):
        super().__init__()
        self.board_copy = deepcopy(self.board)
    # def __str__(self):
    #    return super().__str__()
    # def add_one(self):
    #     self.board[1 , 1] = 9

    def check_board(self, index, row, col):
        is_valid = True
        if np.any(self.board[:, col] == index):
            is_valid = False

        if np.any(self.board[row, :] == index):
            is_valid = False

        frow = row // 3 * 3
        fcol = col // 3 * 3
        small_square = self.board[frow: frow + 3, fcol: fcol + 3]
        if np.any(small_square == index):
            is_valid = False

        return is_valid

    def find_zero(self):
        first_occurence = np.where(self.board == 0)
        if len(first_occurence[0]) != 0:
            first_occurrence_row = first_occurence[0][0]
            first_occurrence_column = first_occurence[1][0]
            return first_occurrence_row, first_occurrence_column
        else:
            return -1, -1

    def solve(self):
        i, j = CompletedBoard.find_zero(self)
        if i == -1:
            return True
        for guess in range(1, 10):
            valid = CompletedBoard.check_board(self, guess, i, j)
            if valid:
                self.board[i][j] = guess
                if CompletedBoard.solve(self):
                    return True
            self.board[i][j] = 0
        return False

    def count_num_zeros(self):
        # counts number of zeros in the board
        count = np.count_nonzero(self.board == 0)
        return count

    def solve_copy(self, board):
        i, j = CompletedBoard.find_zero_copy(self, board)
        if i == -1:
            return True
        for guess in range(1, 10):
            valid = CompletedBoard.check_board_copy(self, board, guess, i, j)
            if valid:
                board[i][j] = guess
                if CompletedBoard.solve_copy(self, board):
                    return True
            board[i][j] = 0
        return False

    def check_board_copy(self, board, index, row, col):
        is_valid = True
        if np.any(board[:, col] == index):
            is_valid = False

        if np.any(board[row, :] == index):
            is_valid = False

        frow = row // 3 * 3
        fcol = col // 3 * 3
        small_square = board[frow: frow + 3, fcol: fcol + 3]
        if np.any(small_square == index):
            is_valid = False

        return is_valid

    def find_zero_copy(self, board):
        # return first instance of 0
        first_occurence = np.where(board == 0)
        if len(first_occurence[0]) != 0:
            first_occurrence_row = first_occurence[0][0]
            first_occurrence_column = first_occurence[1][0]
            return first_occurrence_row, first_occurrence_column
        else:
            return -1, -1

    def generate_board(self):
        i, j = CompletedBoard.find_zero(self)
        while i != -1:
            ran_row = random.randint(0, 8)
            ran_col = random.randint(0, 8)
            ran_num = random.randint(1, 9)
            board_copy = self.board.copy()
            if CompletedBoard.check_board(self, ran_num, ran_row, ran_col) is False:
                self.board[ran_row][ran_col] = 0
                continue
            else:
                self.board[ran_row][ran_col] = ran_num
            if CompletedBoard.solve_copy(self, board_copy) is False:
                self.board[ran_row][ran_col] = 0
            num_zeros = CompletedBoard.count_num_zeros(self)
            if num_zeros < 75:
                CompletedBoard.solve(self)
            i, j = CompletedBoard.find_zero(self)

        return self.board


# b = CompletedBoard()
# b.generate_board()
# print(b)