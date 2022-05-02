from finalizeboard import FinalizeBoard
import numpy as np
class PlayBoard(FinalizeBoard):
    def __init__(self):
        super().__init__()
    def print_sudoku_board(self, board):
        m = ''
        m += ('---------------------------------\n')
        for i in range(9):
            for j in range(9):
                if j == 0:
                    if board[i, j] != 0:
                        m += f'| {board[i, j]} '
                        m.join(m)
                    else:
                        m += f'|   '
                        m.join(m)
                elif (j - 2) % 3 == 0:
                    if board[i, j] != 0:
                        m += f' {board[i, j]} | '
                        m.join(m)
                    else:
                        m += f'   | '
                        m.join(m)
                else:
                    if board[i, j] != 0:
                        m += f' {board[i, j]} '
                        m.join(m)
                    else:
                        m += f'   '
                        m.join(m)
            m += ('\n')
            m.join(m)
            if (i - 2) % 3 == 0:
                m += ('---------------------------------\n')
                m.join(m)
        return m
    def generate_playable_board(self, complete_dif, finalize_dif):
        b = FinalizeBoard()
        solution, completed_board = FinalizeBoard.remove_nums(b, complete_dif, finalize_dif)
        self.board = completed_board
        solution = solution.reshape(9, 9)
        return solution, self.board
    def difficulty(self):
        choose_difficulty_bool = True
        print('Choose Difficulty')
        print('Enter 1 for Easy')
        print('Enter 2 for Medium')
        print('Enter 3 for Hard')
        print('As the difficulty increases, the longer it takes for the board to generate')
        difficulty = 0
        while choose_difficulty_bool:
            difficulty =  int(input('Enter Value: '))
            if difficulty > 3 or difficulty < 1:
                print('Try Again')
            else:
                choose_difficulty_bool = False
        if difficulty == 1:
            return 75, 40
        elif difficulty == 2:
            return 70, 45
        else:
            return 65, 50

    def play_board(self):
        complete_dif, finalize_dif = PlayBoard.difficulty(self)
        solution, playable_board = PlayBoard.generate_playable_board(self, complete_dif, finalize_dif)
        while np.count_nonzero(self.board == 0) > 0:
            print(PlayBoard.print_sudoku_board(self, self.board))
            row = int(input('Enter row: ')) - 1
            col = int(input('Enter column: ')) - 1
            value = int(input('Enter value: '))
            if self.board[row, col] == 0:
                if solution[row, col] != value:
                    print('That is Incorect. Try Again')
                else:
                    self.board[row, col] = value
            else:
                print('That Space Already Has a Value. Try Again')




b = PlayBoard()

b.play_board()