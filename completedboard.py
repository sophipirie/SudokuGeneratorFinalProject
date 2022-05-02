from blankboard import BlankBoard
import random
import numpy as np
from copy import deepcopy

class CompletedBoard(BlankBoard):
    """ Generates Full Completed Sudoku Board """
    def __init__(self):
        super().__init__()
        self.board_copy = deepcopy(self.board)

    def count_num_zeros(self):
        # counts number of zeros in the board
        count = np.count_nonzero(self.board == 0)
        return count

    def solve(self, board):
        # solves sudoku board through back tracking
        i, j = CompletedBoard.find_zero(self, board)
        if i == -1:
            return True
        for guess in range(1, 10):
            valid = CompletedBoard.check_board(self, board, guess, i, j)
            if valid:
                board[i, j] = guess
                if CompletedBoard.solve(self, board):
                    return True
            board[i, j] = 0
        return False

    def check_board(self, board, index, row, col):
        # checks if index placement does not conflict with other values in the sudoku board
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

    def find_zero(self, board):
        # return first instance of 0
        first_occurence = np.where(board == 0)
        if len(first_occurence[0]) != 0:
            first_occurrence_row = first_occurence[0][0]
            first_occurrence_column = first_occurence[1][0]
            return first_occurrence_row, first_occurrence_column
        else:
            return -1, -1

    def generate_board(self, completed_dif):
        # generates Completed Sudoku board by placing random numbers and checking if the board is solveable once placed
        # the completed_dif variable determines how many random numbers are place
        # until the board will be completely solved

        i, j = CompletedBoard.find_zero(self, self.board)
        while i != -1:
            # generates random numbers
            ran_row = random.randint(0, 8)
            ran_col = random.randint(0, 8)
            ran_num = random.randint(1, 9)

            # checks if this placement would work on the board
            board_copy = self.board.copy()
            if CompletedBoard.check_board(self, self.board, ran_num, ran_row, ran_col) is False:
                self.board[ran_row][ran_col] = 0
                continue
            else:
                self.board[ran_row][ran_col] = ran_num

            # uses a copy of the board to check if this placement of the value would create a solvable board
            if CompletedBoard.solve(self, board_copy) is False:
                self.board[ran_row][ran_col] = 0

            # counts the remaining spaces in the sudoku board that do not have a value yet
            # once the number of spaces reaches the completed_dif value, the rest of the board is solved
            num_zeros = CompletedBoard.count_num_zeros(self)
            if num_zeros < completed_dif:
                CompletedBoard.solve(self, self.board)

            i, j = CompletedBoard.find_zero(self, self.board)

        return self.board
