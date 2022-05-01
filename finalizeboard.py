import copy

from completedboard import CompletedBoard
import random
import numpy as np
class FinalizeBoard(CompletedBoard):
    def __init__(self):
        super().__init__()
    def generate_completeboard(self):
        self.board = CompletedBoard.generate_board(self)

    def find_num_solutions(self, board_copy, row, col):
        for n in range(1, 10):
            if CompletedBoard.check_board_copy(self, board_copy, n, row, col):
                board_copy[row, col] = n

                if CompletedBoard.solve_copy(self, board_copy):
                    #print(board_copy)
                    # return board_copy
                    return board_copy

                board_copy[row, col] = 0

        return False
    def find_next_zero(self, board, x):
        y = 1
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:
                    if y == x:
                        return (row, col)
                    y += 1

        return False

    def check_unique(self, final_solution):
        num_zeros = np.count_nonzero(self.board == 0)
        solution_lst =[(np.zeros((1, 81))).astype(int)]
        counts_solution = 0
        a =[]

        for i in range(1, num_zeros + 1):
            board_copy = self.board.copy()
            a = board_copy.copy()
            _row, _col = FinalizeBoard.find_next_zero(self, board_copy, i)
            solution = FinalizeBoard.find_num_solutions(self, board_copy, _row, _col)
            solution = solution.ravel()
            # print('solution', solution)
            # print('final solution', final_solution)
            #if np.all(final_solution == solution) is False:
            print('new start')
            for x in range(81):
                if solution[x] != final_solution[x]:
                        print('false')
                        return False
            # if solution is not False:
            #     solution = solution.ravel()
            #
            #     in_solution_list = False
            #
            #     print('solution list[0]', solution_lst[0])
            #     print('solutio', solution_lst)
            #     if np.count_nonzero(solution_lst[0] == 0) == 81:
            #         solution_lst[0] = solution
            #         print('solution list', solution_lst)
            #         print('no more zeros')
            #     else:
            #         for solution_row in solution_lst:
            #             if np.all(solution == solution_row) is False:
            #                 in_solution_list = True
            #     if in_solution_list:
            #
            #         solution_lst = np.vstack((solution_lst, solution))
            #         print('solution list', solution_lst)
            #
            # print('solution list length', len(solution_lst))
            # print(solution_lst)
            # if len(solution_lst) > 1 and len(solution_lst) != 81:
            #     print('solution list: ', solution_lst)
            #     print('length list: ', len(solution_lst))
            #     print('False: ', a)
            #     return False
        #print(a)
        return True
    def remove_nums(self):
        FinalizeBoard.generate_board(self)
        print(self.board)
        final_solution = self.board.copy()
        final_solution = final_solution.ravel()
        while CompletedBoard.count_num_zeros(self) < 40:
                ran_row = random.randint(0, 8)
                ran_col = random.randint(0, 8)
                if self.board[ran_row, ran_col] != 0:
                    n = self.board[ran_row, ran_col]
                    self.board[ran_row, ran_col] = 0
                    print('new')
                    # # x = FinalizeBoard.check_unique(self)
                    # # print(x)
                    # #if len(FinalizeBoard.check_unique(self)) != 1:
                    # if FinalizeBoard.check_unique(self) > 1:
                    #     self.board[ran_row, ran_col] = n
                    # else:
                    #     print(self.board)
                    if FinalizeBoard.check_unique(self, final_solution) is False:
                        self.board[ran_row, ran_col] = n
                        print('is false', self.board)
                    else:
                        print(self.board)

        #return self.board






b = FinalizeBoard()
#b.generate_completeboard()
b.remove_nums()
print(b)
# b1 = FinalizeBoard()
# b1.generate_completeboard()
# print(b1)