import random
import numpy as np
board = (np.zeros((9, 9))).astype(int)


def print_board(board):
        print('---------------------------------------')
        for i in range(9):
                for j in range(9):
                        if j == 0:
                                print('| ', board[i][j], end="   ")
                        elif (j - 2) % 3 == 0:
                                print(board[i][j], ' |', end="")
                        else:
                                print(board[i][j],'  ', end="")
                print('')
                if (i - 2) % 3 == 0:
                        print('---------------------------------------')

def check_board(board, index, row, col):
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

def find_zero(board):
        # return first instance of 0
        first_occurence = np.where(board == 0)
        if len(first_occurence[0]) != 0:
                first_occurrence_row = first_occurence[0][0]
                first_occurrence_column = first_occurence[1][0]
                return first_occurrence_row, first_occurrence_column
        else:
                return -1, -1

def solve(board):
        i, j = find_zero(board)
        if i == -1:
                return True
        for guess in range(1, 10):
                valid = check_board(board, guess, i, j)
                if valid:
                        board[i][j] = guess
                        if solve(board):
                                return True
                board[i][j] = 0
        return False

def count_num_zeros(board):
        #counts number of zeros in the board
        count = np.count_nonzero(board == 0)
        return count

def generate_board(board):
        i, j = find_zero(board)
        while i != -1:
                ran_row = random.randint(0, 8)
                ran_col = random.randint(0, 8)
                ran_num = random.randint(1, 9)
                board_copy = board.copy()
                if check_board(board, ran_num, ran_row, ran_col) is False:
                        board[ran_row][ran_col] = 0
                        continue
                else:
                        board[ran_row][ran_col] = ran_num
                if solve(board_copy) is False:
                        board[ran_row][ran_col] = 0
                num_zeros = count_num_zeros(board)
                if num_zeros < 70:
                        solve(board)
                i, j = find_zero(board)
generate_board(board)
print_board(board)





