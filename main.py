import random
import numpy as np
board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
# board = [[1, 2, 3, 4, 5, 0, 0, 0, 0],
#         [6, 7, 8, 9, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 6, 0, 0, 8, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

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


# def check_row(board, index, row, col):
#         for cols in range(9):
#                 if cols != col and board[row][cols] == index:
#                         return False
# def check_col(board, index, row, col):
#         for rows in range(9):
#                 if rows != row and board[rows][col] == index:
#                         return False
# def check_box(board, index, row, col):
#         frow = row // 3 * 3
#         fcol = col // 3 * 3
#         for i in range(frow, frow + 3):
#                 for j in range(fcol, fcol + 3):
#                         if i == row and j == col:
#                                 continue
#                         if index == board[i][j]:
#                                 return False

def check_board(board, index, row, col):
        is_valid = True

        for cols in range(9):
                if cols != col and board[row][cols] == index:
                        is_valid = False
        for rows in range(9):
                if rows != row and board[rows][col] == index:
                        is_valid = False
        frow = row // 3 * 3
        fcol = col // 3 * 3
        for i in range(frow, frow + 3):
                for j in range(fcol, fcol + 3):
                        if i == row and j == col:
                                continue
                        if index == board[i][j]:
                                is_valid = False

        return is_valid


def find_zero(board):
        for i in range(9):
                for j in range(9):
                        if board[i][j] == 0:
                                return i , j
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
        count = 0
        for i in range(9):
                for j in range(9):
                        if board[i][j] == 0:
                                count +=1

        return count

def generate_board(board):
        i, j = find_zero(board)
        while i != -1:
                ran_row = random.randint(0, 8)
                ran_col = random.randint(0, 8)
                ran_num = random.randint(1, 9)
                board[ran_row][ran_col] = ran_num
                board_copy = board.copy()
                if check_board(board, ran_num, ran_row, ran_col) is False:
                        board[ran_row][ran_col] = 0
                        continue
                if solve(board_copy) is False:
                        board[ran_row][ran_col] = 0

                num_zeros = count_num_zeros(board)
                if num_zeros < 65:
                        solve(board)
                i, j = find_zero(board)

generate_board(board)
print_board(board)



