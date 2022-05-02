#old commit file no longer used in final code but I want to show my progress

import random
import numpy as np
from copy import deepcopy
board = (np.zeros((9, 9))).astype(int)
class Board:
        def __init__(self):
                self.board = (np.zeros((9, 9))).astype(int)
                self.board_copy = deepcopy(self.board)
        def __str__(self):
                m =''
                m += ('----------------------------------\n')
                for i in range(9):
                        for j in range(9):
                                if j == 0:
                                        m += f'| {self.board[i][j]} '
                                        m.join(m)
                                elif (j - 2) % 3 == 0:
                                        m += f' {self.board[i][j]} | '
                                        m.join(m)
                                else:
                                        m += f' {self.board[i][j]} '
                                        m.join(m)
                        m += ('\n')
                        m.join(m)
                        if (i - 2) % 3 == 0:
                                m += ('----------------------------------\n')
                                m.join(m)
                return m

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
                # return first instance of 0
                first_occurence = np.where(self.board == 0)
                if len(first_occurence[0]) != 0:
                        first_occurrence_row = first_occurence[0][0]
                        first_occurrence_column = first_occurence[1][0]
                        return first_occurrence_row, first_occurrence_column
                else:
                        return -1, -1

        def solve(self):
                i, j = Board.find_zero(self)
                if i == -1:
                        return True
                for guess in range(1, 10):
                        valid = Board.check_board(self, guess, i, j)
                        if valid:
                                self.board[i][j] = guess
                                if Board.solve(self):
                                        return True
                        board[i][j] = 0
                return False

        def count_num_zeros(self):
                #counts number of zeros in the board
                count = np.count_nonzero(self.board == 0)
                return count

        def solve_copy(self, board):
                i, j = Board.find_zero_copy(self, board)
                if i == -1:
                        return True
                for guess in range(1, 10):
                        valid = Board.check_board_copy(self, board, guess, i, j)
                        if valid:
                                board[i][j] = guess
                                if Board.solve_copy(self, board):
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
                i, j = Board.find_zero(self)
                while i != -1:
                        ran_row = random.randint(0, 8)
                        ran_col = random.randint(0, 8)
                        ran_num = random.randint(1, 9)
                        board_copy = self.board.copy()
                        #print(self.board_copy)
                        if Board.check_board(self, ran_num, ran_row, ran_col) is False:
                                self.board[ran_row][ran_col] = 0
                                continue
                        else:
                                self.board[ran_row][ran_col] = ran_num
                        if Board.solve_copy(self, board_copy) is False:
                                self.board[ran_row][ran_col] = 0
                        num_zeros = Board.count_num_zeros(self)
                        if num_zeros < 70:
                                Board.solve(self)
                        i, j = Board.find_zero(self)
# generate_board(board)
# print_board(board)
b = Board()
b.generate_board()
print(b)




