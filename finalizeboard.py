import copy

from completedboard import CompletedBoard
import random
import numpy as np
class FinalizeBoard(CompletedBoard):
    def __init__(self):
        super().__init__()
    def generate_completeboard(self, completed_dif):
        self.board = CompletedBoard.generate_board(self, completed_dif)

    def find_num_solutions(self, board_copy, row, col):
        for n in range(1, 10):
            if CompletedBoard.check_board_copy(self, board_copy, n, row, col):
                board_copy[row, col] = n
                if CompletedBoard.solve_copy(self, board_copy):
                    return board_copy
                board_copy[row, col] = 0

        return False

    def find_next_zero(self, board, x):
        check_value = 0
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:
                    if check_value == x:
                        return (row, col)
                    check_value += 1

        return False

    def check_unique(self, final_solution):
        num_zeros = np.count_nonzero(self.board == 0)

        for i in range(0, num_zeros ):
            board_copy = self.board.copy()
            _row, _col = FinalizeBoard.find_next_zero(self, board_copy, i)
            solution = FinalizeBoard.find_num_solutions(self, board_copy, _row, _col)
            solution = solution.ravel()
            for x in range(81):
                if solution[x] != final_solution[x]:
                        return False
        return True

    def remove_nums(self, completed_dif, finalize_dif):
        FinalizeBoard.generate_board(self, completed_dif)
        final_solution = self.board.copy()
        final_solution = final_solution.ravel()
        while CompletedBoard.count_num_zeros(self) < finalize_dif:
                ran_row = random.randint(0, 8)
                ran_col = random.randint(0, 8)
                if self.board[ran_row, ran_col] != 0:
                    n = self.board[ran_row, ran_col]
                    self.board[ran_row, ran_col] = 0
                    if FinalizeBoard.check_unique(self, final_solution) is False:
                        self.board[ran_row, ran_col] = n
        return final_solution, self.board

